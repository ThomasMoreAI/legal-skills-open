#!/usr/bin/env bash
# Migrate local SQLite DB to Turso
# Usage: bash scripts/migrate_to_turso.sh <turso-db-name>
#
# Prerequisites:
#   - turso CLI installed (curl -sSfL https://get.tur.so/install.sh | bash)
#   - turso auth login done
#   - Local DB exists at db/custom.db
#   - Run: bun add @prisma/adapter-libsql @libsql/client

set -euo pipefail

DB_NAME="${1:-thai-law-hub}"
LOCAL_DB="db/custom.db"

if [ ! -f "$LOCAL_DB" ]; then
  echo "❌ Local DB not found at $LOCAL_DB"
  echo "   Run: python scripts/rebuild_legal_db.py && cp data/thai_legal_db.sqlite $LOCAL_DB"
  exit 1
fi

echo "📦 Checking Turso database '$DB_NAME'..."
if ! turso db show "$DB_NAME" &>/dev/null; then
  echo "📦 Creating Turso database '$DB_NAME'..."
  turso db create "$DB_NAME" --location sin
fi

DB_URL=$(turso db show "$DB_NAME" --url)
echo "🔗 Database URL: $DB_URL"

echo "📤 Exporting local DB to SQL..."
DUMP_FILE="/tmp/thai_law_dump.sql"
sqlite3 "$LOCAL_DB" .dump > "$DUMP_FILE"

# Remove PRAGMA statements and transaction markers that Turso may not support
sed -i '/PRAGMA /d; /BEGIN TRANSACTION;/d; /^COMMIT;$/d' "$DUMP_FILE"

echo "📤 Importing to Turso..."
turso db shell "$DB_NAME" < "$DUMP_FILE"

echo "✅ Verifying..."
LAW_COUNT=$(turso db shell "$DB_NAME" "SELECT COUNT(*) FROM laws;")
SECTION_COUNT=$(turso db shell "$DB_NAME" "SELECT COUNT(*) FROM law_sections;")
JUDGMENT_COUNT=$(turso db shell "$DB_NAME" "SELECT COUNT(*) FROM case_judgments;")

echo "  Laws: $LAW_COUNT"
echo "  Sections: $SECTION_COUNT"
echo "  Judgments: $JUDGMENT_COUNT"

# Recreate FTS5 indexes (sometimes Turso needs this)
echo "🔍 Recreating FTS5 indexes..."
turso db shell "$DB_NAME" << 'EOF' || true
DROP TABLE IF EXISTS law_sections_fts;
CREATE VIRTUAL TABLE law_sections_fts USING fts5(
  section_text, article_key, law_id UNINDEXED, section_id UNINDEXED,
  content='law_sections', content_rowid='section_id'
);
INSERT INTO law_sections_fts(section_text, article_key, law_id, section_id)
  SELECT section_text, COALESCE(article_key, ''), law_id, section_id FROM law_sections;

DROP TABLE IF EXISTS case_judgments_fts;
CREATE VIRTUAL TABLE case_judgments_fts USING fts5(
  fact, decision, case_number, judgment_id UNINDEXED, category UNINDEXED,
  content='case_judgments', content_rowid='judgment_id'
);
INSERT INTO case_judgments_fts(fact, decision, case_number, judgment_id, category)
  SELECT COALESCE(fact,''), COALESCE(decision,''), COALESCE(case_number,''), judgment_id, COALESCE(category,'')
  FROM case_judgments;
EOF

echo ""
echo "🎉 Migration complete!"
echo ""
echo "Next steps:"
echo "1. Get auth token:  turso db tokens create $DB_NAME"
echo "2. Update .env:"
echo "   DATABASE_URL=$DB_URL"
echo "   TURSO_AUTH_TOKEN=<token>"
echo "3. Switch schema:   cp prisma/schema.turso.prisma prisma/schema.prisma"
echo "4. Install adapter: bun add @prisma/adapter-libsql @libsql/client"
echo "5. Regenerate:      bun run db:generate"
echo "6. Test local:      bun run dev"
