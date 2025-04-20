import orjson
from typing import Callable
from asyncpg.pgproto.pgproto import UUID
from pydantic import BaseModel


def orjson_uuid_decoder(obj):
    """
    Custom ORJSON decoder for UUID objects.
    """
    if isinstance(obj, UUID):
        return str(obj)
    raise TypeError(f"Type {type(obj)} is not serializable")


def json_dump(data: any) -> dict:
    """
    Serialize data to JSON using orjson with custom UUID handling. 
    """
    x = orjson.dumps(data, default=orjson_uuid_decoder).decode("utf-8")
    return orjson.loads(x)


json_data : Callable[[BaseModel], dict] = lambda m: {"data": json_dump(m.model_dump())}
