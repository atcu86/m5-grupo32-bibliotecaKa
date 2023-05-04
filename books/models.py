from django.db import models
from users.models import User
import uuid


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    published_date = models.DateField()
    publishing_company = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    quantity = models.IntegerField()
    days_to_borrow = models.IntegerField(default=14)

    genres = models.ManyToManyField("genres.Genre", related_name="books")

    user_following = models.ManyToManyField(
        User, through="user_following.UserFollowing", related_name="books"
    )
