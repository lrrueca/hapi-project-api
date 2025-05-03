from tortoise import fields
from tortoise.models import Model
from .mixins import TimestampMixin


class AccountType(Model, TimestampMixin):
    id = fields.IntField(primary_key=True, auto_generated=True)
    name = fields.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        table = "account_type"
        ordering = ["name"]
        indexes = [
            ("name",),
        ]


class Account(Model, TimestampMixin):
    id = fields.UUIDField(primary_key=True, auto_generated=True)
    name = fields.CharField(max_length=255)
    isrcode = fields.CharField(max_length=50, null=True)
    sapcode = fields.CharField(max_length=50, null=True)
    account_type = fields.ForeignKeyField(
        "models.AccountType", related_name="accounts", on_delete=fields.CASCADE
    )
    supplier = fields.ForeignKeyField(
        "models.Account", related_name="retailers", null=True, on_delete=fields.CASCADE
    )

    def __str__(self):
        return f"{self.name} ({self.account_type})"

    class Meta:
        table = "account"
        ordering = ["name"]
        indexes = [
            ("name",),
        ]
