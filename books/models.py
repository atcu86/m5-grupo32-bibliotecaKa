from django.db import models
import uuid


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    published_date = models.DateField()

    user_following = models.ForeignKey(
        "user_following.UserFollowing", on_delete=models.CASCADE, related_name="books"
    )
