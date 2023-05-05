import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_employee = models.BooleanField(null=True, default=False)
    is_allowed_lending = models.BooleanField(null=True, default=True)
    date_block = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("id",)
