from ..models import Account


async def update_account_handler(id: int, data: dict):
    """
    Updates account information in the database.
    Args:
        id (int): The ID of the account to update.
        data (dict): A dictionary containing the data to update.
    Returns:
        None
    """
    entity: Account = await Account.get(id=id)
    entity.update_from_dict(data)
    await entity.save()
