from tortoise.contrib.pydantic import PydanticListModel
from tortoise.queryset import QuerySet

from ..models import Account, account_read_list_model
from ....application.decoders import json_data


async def get_all_accounts_handler():
    """
    Retrieves all accounts from the database.
    Returns:
        dict: A serialized list of accounts.
    """
    qs: QuerySet[Account] = Account.all()
    pm: PydanticListModel = await account_read_list_model.from_queryset(qs)
    content = json_data(pm)
    return content
