from django.db import models
import uuid


class BookCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    is_available = models.BooleanField(null=True, default=True)
