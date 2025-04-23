from tortoise import fields


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


class AddressMixin:
    address = fields.CharField(max_length=255, null=True)
    city = fields.CharField(max_length=100, null=True)
    state = fields.CharField(max_length=100, null=True)
    country = fields.CharField(max_length=100, null=True)
    postal_code = fields.CharField(max_length=20, null=True)
