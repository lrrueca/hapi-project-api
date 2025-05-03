from tortoise.contrib.pydantic import PydanticModel
from tortoise.queryset import QuerySetSingle

from ..models import Account, account_read_model
from ....application.decoders import json_data


async def get_account_by_id_handler(id: str) -> dict:
    """
    Retrieves an account by its ID.
    Args:
        id (str): The ID of the account to retrieve.
    Returns:
        dict: Serialized account data.
    """
    qs: QuerySetSingle[Account | None] = Account.get_or_none(id=id)
    pm: PydanticModel = await account_read_model.from_queryset_single(qs)
    content = json_data(pm)
    return content
