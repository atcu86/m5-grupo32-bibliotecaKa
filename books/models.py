from django.db import models
from users.models import User
import uuid


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    published_date = models.DateField()

    user_following = models.ManyToManyField(
        User, through="user_following.UserFollowing", related_name="books"
    )
