import bcrypt
from asyncpg.pgproto.pgproto import UUID
from tortoise.contrib.pydantic import PydanticModel
from ..models import User, user_write_model


async def create_user_handler(data: dict) -> UUID:
    """
    Creates a new user.
    This function takes a dictionary containing user data, hashes the password,
    and saves the user to the database.
    Args:
        data (dict): A dictionary containing user data, including the password.
    Returns:
        UUID: The UUID of the created user.
    """
    # extract the password from the data
    data_pwd = data["password"]

    # Hash the password
    hash_pwd: bytes = bcrypt.hashpw(data_pwd.encode("utf-8"), bcrypt.gensalt())

    # Extract and process user data
    _data: dict = {
        **data,
        "hash_pwd": hash_pwd,  # use the hashed password for hash_pwd key
    }

    # Remove the password key from the user data
    _data.pop("password")  # remove the original password key

    # Validate and transform the user data
    pm: PydanticModel = user_write_model.model_validate(_data)

    entity: User = User(**pm.model_dump())
    await entity.save()

    return entity.id
