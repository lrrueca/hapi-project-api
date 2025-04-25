from tortoise.contrib.pydantic import PydanticListModel, PydanticModel, pydantic_queryset_creator, pydantic_model_creator
from ...infrastructure.models.account import AccountType


account_type_read_list_model: type[PydanticListModel] = pydantic_queryset_creator(AccountType, exclude=("created_at", "modified_at"))
account_type_read_model: type[PydanticModel] = pydantic_model_creator(AccountType, exclude=("created_at", "modified_at"))
account_type_write_model: type[PydanticModel] = pydantic_model_creator(AccountType, exclude=("id", "created_at", "modified_at"))
