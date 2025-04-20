from asyncpg.pgproto.pgproto import UUID
from ..models import User


async def delete_user_handler(id: int | str | UUID) -> None:
    """
    Delete a user by ID.
    Args:
        id (int | str | UUID): The ID of the user to delete.
    Returns:
        None
    """
    entity = await User.get(id=id)
    await entity.delete()
    return None
