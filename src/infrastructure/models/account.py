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
