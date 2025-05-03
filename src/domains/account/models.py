from tortoise.contrib.pydantic import PydanticListModel, PydanticModel, pydantic_queryset_creator, pydantic_model_creator
from ...infrastructure.models.account import Account


account_read_list_model: type[PydanticListModel] = pydantic_queryset_creator(Account, exclude=("created_at", "modified_at",))
account_read_model: type[PydanticModel] = pydantic_model_creator(Account, exclude=("created_at", "modified_at"))
account_write_model: type[PydanticModel] = pydantic_model_creator(Account, exclude=("id", "created_at", "modified_at"))


