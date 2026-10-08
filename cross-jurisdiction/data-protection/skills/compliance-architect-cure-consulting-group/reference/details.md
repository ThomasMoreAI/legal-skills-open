# compliance-architect: detailed reference

> Read when writing client-side storage code, Firestore rules for regulated collections, or the role-claim function for the `compliance-architect` skill.

## Contents
- Step 6: Platform-Specific Compliance Patterns

## Step 6: Platform-Specific Compliance Patterns

### Android

```kotlin
// androidx.security:security-crypto (EncryptedSharedPreferences) is deprecated since 1.1.0 (2025).
// Use a Tink AEAD whose keyset is wrapped by an Android Keystore master key, and persist with DataStore.
AeadConfig.register()
val aead: Aead = AndroidKeysetManager.Builder()
    .withSharedPref(context, "tink_keyset", "tink_prefs")   // stores only the Keystore-wrapped keyset
    .withKeyTemplate(KeyTemplates.get("AES256_GCM"))
    .withMasterKeyUri("android-keystore://cure_master_key")
    .build()
    .keysetHandle
    .getPrimitive(RegistryConfiguration.get(), Aead::class.java)
// Encrypt values before writing to DataStore; bind ciphertext to the key name as associated data.
val ciphertext = aead.encrypt(plaintext, "consent_state".toByteArray())

// Room encryption with SQLCipher (net.zetetic:sqlcipher-android): derive the passphrase once,
// store it encrypted with the Tink AEAD above — never regenerate per launch.
val factory = SupportOpenHelperFactory(passphrase)
Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .openHelperFactory(factory)
    .build()

// COPPA: analytics and crash identifiers off for child accounts unless the parent consented
if (user.isUnder13) {
    Firebase.analytics.setAnalyticsCollectionEnabled(false)
    Firebase.crashlytics.isCrashlyticsCollectionEnabled = false
}
```

### iOS

```swift
// Keychain for RESTRICTED data
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "healthRecordEncryptionKey",
    kSecValueData as String: keyData,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
]
SecItemAdd(query as CFDictionary, nil)

// COPPA: disable tracking for child accounts
if user.isUnder13 {
    Analytics.setAnalyticsCollectionEnabled(false)
    Crashlytics.crashlytics().setCrashlyticsCollectionEnabled(false)
}

// HIPAA: blur screen content when app enters background
func sceneWillResignActive(_ scene: UIScene) {
    let blurEffect = UIBlurEffect(style: .light)
    let blurView = UIVisualEffectView(effect: blurEffect)
    blurView.tag = 999
    window?.addSubview(blurView)
}
```

### Firestore Security Rules for PHI

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Health records: only the patient or authorized providers
    match /health_records/{recordId} {
      allow read: if request.auth != null
        && (request.auth.uid == resource.data.patientId
            || request.auth.token.role == 'provider'
            && request.auth.uid in resource.data.authorizedProviders);
      allow write: if request.auth != null
        && request.auth.token.role == 'provider'
        && request.auth.uid in resource.data.authorizedProviders;
      allow delete: if false; // PHI cannot be deleted via client — admin function only
    }

    // Audit logs: convenience copy only (system of record is a locked log bucket).
    // Written by Cloud Functions via the Admin SDK, which bypasses rules; clients can never forge entries.
    match /audit_logs/{logId} {
      allow create: if false;
      allow read: if request.auth.token.role == 'admin'
                  || request.auth.token.role == 'compliance_officer';
      allow update, delete: if false;
    }

    // Consent records: append-only, written by a Cloud Function with a server timestamp
    match /consent_records/{recordId} {
      allow create: if false;
      allow read: if request.auth.uid == resource.data.userId
                  || request.auth.token.role == 'admin';
      allow update, delete: if false;
    }
  }
}
```

### Firebase Auth Custom Claims for Compliance Roles

```typescript
// Cloud Functions v2 callable: set compliance roles and audit the change
import { onCall, HttpsError } from "firebase-functions/v2/https";
import { getAuth } from "firebase-admin/auth";
import { getFirestore, FieldValue } from "firebase-admin/firestore";
import { randomUUID } from "node:crypto";

const VALID_ROLES = ["user", "provider", "admin", "compliance_officer"];

export const setComplianceRole = onCall({ enforceAppCheck: true }, async (request) => {
  if (request.auth?.token.role !== "admin") {
    throw new HttpsError("permission-denied", "Admin only");
  }
  const { uid, role, reason } = request.data as { uid: string; role: string; reason?: string };
  if (!VALID_ROLES.includes(role)) throw new HttpsError("invalid-argument", "Invalid role");

  await getAuth().setCustomUserClaims(uid, { role });
  // Also emit the same event to the locked Cloud Logging bucket (system of record).
  await getFirestore().collection("audit_logs").add({
    eventId: randomUUID(),
    timestamp: FieldValue.serverTimestamp(),
    actorId: request.auth.uid,
    actorRole: "admin",
    action: "update",
    resource: `users/${uid}`,
    classification: "RESTRICTED",
    fieldsModified: ["customClaims.role"],
    result: "success",
    reason: reason ?? "role_assignment",
  });
});
```
