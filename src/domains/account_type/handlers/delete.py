from ..models import AccountType


async def delete_account_type_handler(id: int) -> None:
    """
    Delete an account type by ID.
    Args:
        id (int): The ID of the account type to delete.
    Returns:
        None
    """
    entity = await AccountType.get(id=id)
    await entity.delete()
    return None
