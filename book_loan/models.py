from django.db import models
import uuid


class BookLoan(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book_copy = models.ForeignKey(
        'book_copy.BookCopy',
        on_delete=models.CASCADE,
        related_name='book_loan'
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='book_loan')
    loan_date = models.DateTimeField(auto_now_add=True)
    max_return_date = models.DateTimeField(blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
