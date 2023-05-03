from django.db import models
from users.models import User
from books.models import Book
import uuid


class UserFollowing(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
