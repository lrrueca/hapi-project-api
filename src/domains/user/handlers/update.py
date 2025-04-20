from asyncpg.pgproto.pgproto import UUID
from ..models import User


async def update_user_handler(id: int | str | UUID, data: dict):
    """
    Updates user information in the database.
    Args:
        id (int | str | UUID): The ID of the user to update.
        data (dict): A dictionary containing the data to update.
    Returns:
        None
    """
    entity: User = await User.get(id=id)
    entity.update_from_dict(data)
    await entity.save()
