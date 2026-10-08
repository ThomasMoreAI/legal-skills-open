# Cookie / Consent Banner — PDPA Compliant

## Design rules (read before copying HTML)

1. **No pre-checked toggles** for anything except "Necessary".
2. **"ยอมรับทั้งหมด" (Accept all) and "ปฏิเสธทั้งหมด" (Reject all) on the same surface, same button style, same colour, same size.** Reject must NOT live behind a "Manage preferences" wall.
3. **Granular toggles** for 4 categories: Necessary / Analytics / Marketing / Personalization.
4. **Withdraw is as easy as give.** Always render a "Cookie preferences" link in the footer that re-opens this banner.
5. **No "by continuing to use the site you agree…"** — that is not valid consent under PDPA Sec 19.
6. **Thai is primary**; English is secondary.

## Copy (use verbatim or adapt)

### Banner heading
- TH: **เราใช้คุกกี้เพื่อให้บริการที่ดียิ่งขึ้น**
- EN: We use cookies to improve your experience

### Body
- TH: เว็บไซต์นี้ใช้คุกกี้และเทคโนโลยีที่คล้ายกันเพื่อให้บริการ วิเคราะห์การใช้งาน และปรับแต่งเนื้อหาให้เหมาะกับท่าน. ท่านสามารถเลือกประเภทคุกกี้ที่ยินยอมให้เราใช้ได้ตามรายการด้านล่าง. การตั้งค่าสามารถเปลี่ยนแปลงได้ทุกเมื่อผ่านลิงก์ "การตั้งค่าคุกกี้" ที่ส่วนล่างของหน้า. รายละเอียดเพิ่มเติมในนโยบายความเป็นส่วนตัวและนโยบายคุกกี้.
- EN: This site uses cookies to deliver services, analyse usage, and personalise content. Choose which categories of cookies we may use below. You can change these settings at any time via the "Cookie preferences" link in the footer. See our Privacy and Cookie Policies for details.

### Categories
| Key | Label TH | Label EN | Default | Locked? |
|---|---|---|---|---|
| necessary | คุกกี้ที่จำเป็น | Strictly necessary | ON | Yes (cannot disable) |
| analytics | คุกกี้เพื่อการวิเคราะห์ | Analytics | OFF | No |
| marketing | คุกกี้เพื่อการตลาด | Marketing | OFF | No |
| personalization | คุกกี้เพื่อปรับแต่งเนื้อหา | Personalization | OFF | No |

### Per-category descriptions
- **คุกกี้ที่จำเป็น / Strictly necessary** — ใช้เพื่อให้เว็บไซต์ทำงานได้ปกติ เช่น เก็บสถานะการเข้าสู่ระบบ ตะกร้าสินค้า ความปลอดภัย. *ปิดไม่ได้.*
- **คุกกี้เพื่อการวิเคราะห์ / Analytics** — เก็บสถิติการใช้งานโดยไม่ระบุตัวตน เช่น หน้าที่นิยม เวลาที่ใช้ ผ่าน Google Analytics, Plausible. ช่วยให้เราปรับปรุงเว็บไซต์.
- **คุกกี้เพื่อการตลาด / Marketing** — ใช้แสดงโฆษณาที่เกี่ยวข้องบนเว็บไซต์อื่น ผ่าน Meta Pixel, Google Ads, Line Ads. หากท่านปฏิเสธ ท่านจะยังเห็นโฆษณา แต่จะไม่ได้รับการปรับให้ตรงความสนใจ.
- **คุกกี้เพื่อปรับแต่งเนื้อหา / Personalization** — จดจำการตั้งค่าของท่าน เช่น ภาษา ภูมิภาค ธีม.

### Buttons (equal weight — same style, same row, same colour)
- TH: `ปฏิเสธทั้งหมด` | `ตั้งค่า` | `ยอมรับทั้งหมด`
- EN: `Reject all` | `Customize` | `Accept all`

> "Customize" is optional and is NEVER the only path to reject. If you only show two buttons, they must be **Reject all** and **Accept all** with identical styling.

---

## HTML mockup

```html
<!-- bottom-sheet pattern; accessible, equal-weight buttons -->
<aside id="pdpa-banner"
       role="dialog"
       aria-labelledby="pdpa-title"
       aria-describedby="pdpa-body"
       style="position:fixed;inset:auto 0 0 0;background:#fff;border-top:1px solid #e5e7eb;padding:20px;z-index:9999;font-family:'Sarabun','Noto Sans Thai',sans-serif;">

  <h2 id="pdpa-title" style="margin:0 0 8px;font-size:18px;font-weight:600;">
    เราใช้คุกกี้เพื่อให้บริการที่ดียิ่งขึ้น
  </h2>

  <p id="pdpa-body" style="margin:0 0 16px;font-size:14px;line-height:1.6;">
    เว็บไซต์นี้ใช้คุกกี้เพื่อให้บริการ วิเคราะห์การใช้งาน และปรับแต่งเนื้อหา.
    ท่านสามารถเลือกได้ว่าจะยอมรับประเภทใดบ้าง. รายละเอียดเพิ่มเติมใน
    <a href="/privacy">นโยบายความเป็นส่วนตัว</a>.
  </p>

  <!-- granular toggles (collapsed by default; expand via "ตั้งค่า") -->
  <fieldset id="pdpa-categories" hidden style="border:0;padding:0;margin:0 0 16px;">
    <legend class="sr-only">ประเภทคุกกี้</legend>

    <label style="display:flex;gap:8px;padding:8px 0;">
      <input type="checkbox" checked disabled name="necessary">
      <span><strong>คุกกี้ที่จำเป็น</strong> — เปิดถาวร (ปิดไม่ได้)</span>
    </label>

    <label style="display:flex;gap:8px;padding:8px 0;">
      <input type="checkbox" name="analytics"><!-- DEFAULT OFF -->
      <span><strong>คุกกี้เพื่อการวิเคราะห์</strong> — Google Analytics, Plausible</span>
    </label>

    <label style="display:flex;gap:8px;padding:8px 0;">
      <input type="checkbox" name="marketing"><!-- DEFAULT OFF -->
      <span><strong>คุกกี้เพื่อการตลาด</strong> — Meta Pixel, Google Ads</span>
    </label>

    <label style="display:flex;gap:8px;padding:8px 0;">
      <input type="checkbox" name="personalization"><!-- DEFAULT OFF -->
      <span><strong>คุกกี้เพื่อปรับแต่งเนื้อหา</strong> — language, theme</span>
    </label>
  </fieldset>

  <!--
    Equal-weight buttons: SAME style, SAME size, SAME row.
    Order is left-to-right: Reject, Customize, Accept.
    All buttons share class .pdpa-btn so there's no visual hierarchy that nudges Accept.
  -->
  <div style="display:flex;gap:8px;flex-wrap:wrap;">
    <button class="pdpa-btn" data-action="reject-all"
            style="flex:1;min-width:140px;padding:12px 16px;border:1px solid #111;background:#fff;color:#111;font-weight:600;cursor:pointer;">
      ปฏิเสธทั้งหมด
    </button>
    <button class="pdpa-btn" data-action="customize"
            style="flex:1;min-width:140px;padding:12px 16px;border:1px solid #111;background:#fff;color:#111;font-weight:600;cursor:pointer;">
      ตั้งค่า
    </button>
    <button class="pdpa-btn" data-action="accept-all"
            style="flex:1;min-width:140px;padding:12px 16px;border:1px solid #111;background:#111;color:#fff;font-weight:600;cursor:pointer;">
      ยอมรับทั้งหมด
    </button>
  </div>
</aside>

<!-- Persistent footer link so users can WITHDRAW consent later -->
<footer>
  <a href="#" id="pdpa-reopen">การตั้งค่าคุกกี้ / Cookie preferences</a>
</footer>
```

> **Visual hierarchy note.** The Accept button has a darker fill in the mockup above, which is the most common dark-pattern complaint. To be fully audit-safe, make all three buttons the **same fill style** (e.g., all outlined, or all solid in the same colour). Different teams interpret "equal prominence" strictly — when in doubt, give Reject the most prominent style, not Accept.

## Consent record (server-side)

When the user submits choices, persist a consent record. Required fields:

```json
{
  "consent_id": "uuid-v4",
  "subject_id": "user_id or anonymous cookie ID",
  "timestamp_utc": "2026-05-16T03:21:00Z",
  "policy_version": "1.0",
  "purposes": {
    "necessary": true,
    "analytics": false,
    "marketing": false,
    "personalization": false
  },
  "method": "banner-v3",
  "ip_truncated": "203.0.113.0/24",
  "user_agent": "..."
}
```

Retain consent records for the duration of processing + 1 year (for audit).
