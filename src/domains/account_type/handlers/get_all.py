from tortoise.contrib.pydantic import PydanticListModel
from tortoise.queryset import QuerySet

from ..models import AccountType, account_type_read_list_model
from ....application.decoders import json_data


async def get_all_account_types_handler():
    """
    Retrieves all account types from the database.
    Returns:
        dict: A serialized list of account types.
    """
    qs: QuerySet[AccountType] = AccountType.all()
    pm: PydanticListModel = await account_type_read_list_model.from_queryset(qs)
    content = json_data(pm)
    return content
