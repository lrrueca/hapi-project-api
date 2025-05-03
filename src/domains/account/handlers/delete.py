from ..models import Account


async def delete_account_handler(id: int) -> None:
    """
    Delete an account by ID.
    Args:
        id (int): The ID of the account to delete.
    Returns:
        None
    """
    entity = await Account.get(id=id)
    await entity.delete()
    return None
