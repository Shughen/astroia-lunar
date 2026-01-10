"""Script pour appliquer la migration dev_external_id"""

import asyncio
from sqlalchemy import text
from database import engine


async def apply_migration():
    """Applique la migration add_dev_external_id_to_users.sql"""

    async with engine.begin() as conn:
        print("🔧 Applying migration: add_dev_external_id_to_users")

        # Step 1: Add column
        await conn.execute(text("""
            ALTER TABLE users
            ADD COLUMN IF NOT EXISTS dev_external_id TEXT UNIQUE;
        """))
        print("✅ Step 1/2: Column added")

        # Step 2: Create index
        await conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_users_dev_external_id ON users(dev_external_id);
        """))
        print("✅ Step 2/2: Index created")

        print("✅ Migration applied successfully")

        # Verify column exists
        result = await conn.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'users' AND column_name = 'dev_external_id';
        """))
        row = result.fetchone()

        if row:
            print(f"✅ Column verified: {row[0]} ({row[1]}, nullable={row[2]})")
        else:
            print("⚠️  Column not found after migration")


if __name__ == "__main__":
    asyncio.run(apply_migration())
