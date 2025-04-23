from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "id" UUID NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "middle_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "hash_pwd" VARCHAR(255) NOT NULL UNIQUE,
    "phone_number" VARCHAR(15) NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_user_usernam_9987ab" ON "user" ("username");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""
