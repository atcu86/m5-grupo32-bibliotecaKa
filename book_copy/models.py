from django.db import models
from users.models  import User
import uuid


class BookCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    is_available = models.BooleanField(null=True, default=True)
    book_loans =  models.ManyToManyField(User, through="book_loan.BookLoan", related_name="book_copy")
    lending_time_limit = models.IntegerField()