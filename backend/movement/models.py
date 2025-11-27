from django.db import models
from users.models import User
from catalog.models import Book, Copies


class Borrow(models.Model):

    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    copies_id = models.ForeignKey(
        Copies, on_delete=models.SET_NULL, null=True, blank=True
    )
    withdrawal_date = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField()
    return_date = models.DateTimeField(null=True, blank=True)
    fine_paid = models.BooleanField(default=None, null=True, blank=True)


class Requests(models.Model):
    class Type(models.TextChoices):
        BOOKING = "B", "booking"
        RENEWAL = "R", "renewal"
        PURCHASE_SUGGESTION = "PS", "purchase_suggestion"

    class Status(models.TextChoices):
        PEDING = "P", "peding"
        APPROVED = "A", "approved"
        REJECTED = "R", "rejected"

    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    book_id = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True
    )
    type = models.CharField(
        max_length=2, choices=Type.choices, default=Type.BOOKING
    )
    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.PEDING
    )
    order_date = models.DateTimeField(auto_now_add=True)
