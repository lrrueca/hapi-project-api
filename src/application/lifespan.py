import contextlib
from infrastructure.db import db_connect, db_close


@contextlib.asynccontextmanager
async def lifespan(app):
    await db_connect()
    yield
    await db_close()

