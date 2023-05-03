from django.db import models
import uuid
# Create your models here.


class BookCopy(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    # publishing_company = models.CharField(max_length=200)
    # language = models.CharField(max_length=200)
    # lending_time_limit=models.PositiveIntegerField(default=7)
    # is_available=models.BooleanField(null=True, default=True)

    ...


# class Loan(models.Model):

#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='loans')
#     book_copy = models.ForeignKey("book_copy.BookCopy", on_delete=models.CASCADE, related_name='loans')
#     loan_date = models.DateTimeField(auto_now_add=True)
#     max_return_date = models.DateTimeField(null=True, blank=True)
#     returned_date = models.DateField(null=True, blank=True)

#     ...
