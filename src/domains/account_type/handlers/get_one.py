from tortoise.contrib.pydantic import PydanticModel
from tortoise.queryset import QuerySetSingle
from ..models import AccountType, account_type_read_model
from ....application.decoders import json_data


async def get_account_type_by_id_handler(id: str) -> dict:
    """
    Retrieves an account type by its ID.
    Args:
        id (str): The ID of the account type to retrieve.
    Returns:
        dict: Serialized account type data.
    """
    qs: QuerySetSingle[AccountType | None] = AccountType.get_or_none(id=id)
    pm: PydanticModel = await account_type_read_model.from_queryset_single(qs)
    content = json_data(pm)
    return content
