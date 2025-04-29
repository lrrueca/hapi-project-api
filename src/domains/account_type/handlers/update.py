from ..models import AccountType


async def update_account_type_handler(id: int, data: dict):
    """
    Updates account type information in the database.
    Args:
        id (int): The ID of the account type to update.
        data (dict): A dictionary containing the data to update.
    Returns:
        None
    """
    entity: AccountType = await AccountType.get(id=id)
    entity.update_from_dict(data)
    await entity.save()
