from tortoise.contrib.pydantic import PydanticModel
from ..models import AccountType, account_type_write_model


async def create_account_type_handler(data: dict) -> int:
    """
    Creates a new account type.
    Args:
        data (dict): The account type data to create.
    Returns:
        int: The ID of the created account type.
    """
    # Extract and process account type data
    pm: PydanticModel = account_type_write_model.model_validate(data)

    entity: AccountType = AccountType(**pm.model_dump())
    await entity.save()

    return entity.id
