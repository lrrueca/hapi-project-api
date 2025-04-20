import os
from tortoise import Tortoise


db_url = os.getenv("DB_URL")
if not db_url:
    raise ValueError("Environment variable 'DB_URL' is not set.")

config = {
    "connections": {
        "default": db_url,
    },
    "apps": {
        "models": {
            "models": ["src.infrastructure.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def db_connect():
    await Tortoise.init(config=config)
    await Tortoise.generate_schemas()


async def db_close():
    await Tortoise.close_connections()
