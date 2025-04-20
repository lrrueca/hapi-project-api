from tortoise.contrib.pydantic import PydanticModel
from tortoise.queryset import QuerySetSingle

from ..models import User, user_read_model
from ....application.decoders import json_data


async def get_user_by_id_handler(id: str) -> dict:
    """
    Retrieves a user by their ID.
    Args:
        id (str): The ID of the user to retrieve.
    Returns:
        dict: Serialized user data.
    """
    qs: QuerySetSingle[User | None] = User.get_or_none(id=id)
    pm: PydanticModel = await user_read_model.from_queryset_single(qs)
    content = json_data(pm)
    return content
