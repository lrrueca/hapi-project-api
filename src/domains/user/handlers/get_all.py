from tortoise.contrib.pydantic import PydanticListModel
from tortoise.queryset import QuerySet

from ..models import User, user_read_list_model
from ....application.decoders import json_data


async def get_all_users_handler():
    """
    Retrieves all users from the database.
    Returns:
        dict: A serialized list of users.
    """
    qs: QuerySet[User] = User.all()
    pm: PydanticListModel = await user_read_list_model.from_queryset(qs)
    content = json_data(pm)
    return content
