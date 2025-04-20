from tortoise.contrib.pydantic import PydanticListModel, PydanticModel, pydantic_queryset_creator, pydantic_model_creator
from ...infrastructure.models import User


user_read_list_model: type[PydanticListModel] = pydantic_queryset_creator(User, exclude=("created_at", "modified_at"))
user_read_model: type[PydanticModel] = pydantic_model_creator(User, exclude=("hash_pwd","created_at", "modified_at"))
user_create_model: type[PydanticModel] = pydantic_model_creator(User, exclude=("id","created_at", "modified_at"))
