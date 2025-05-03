from tortoise.contrib.pydantic import PydanticModel
from ..models import Account, account_write_model


async def create_account_handler(data: dict) -> int:
    """
    Creates a new account.
    Args:
        data (dict): The account data to create.
    Returns:
        int: The ID of the created account.
    """
    # Extract and process account data
    pm: PydanticModel = account_write_model.model_validate(data)

    entity: Account = Account(**pm.model_dump())
    await entity.save()

    return entity.id
