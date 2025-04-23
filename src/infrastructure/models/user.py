from tortoise import fields
from tortoise.models import Model
from .mixins import TimestampMixin


class User(Model, TimestampMixin):
    id = fields.UUIDField(primary_key=True, auto_generated=True)
    first_name = fields.CharField(max_length=50)
    middle_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=50, unique=True)
    hash_pwd = fields.CharField(max_length=255, unique=True)
    phone_number = fields.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    class Meta:
        table = "user"
        ordering = ["last_name", "middle_name", "first_name"]
        indexes = [
            ("username",),
        ]
