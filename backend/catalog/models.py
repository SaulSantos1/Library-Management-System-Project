from django.db import models


class Book(models.Model):

    isbn = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.ForeignKey()
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keywords = models.CharField(max_length=150)

    def __str__(self):
        return self.isbn


class Copies(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = "A", "Available"
        BORROWED = "B", "Borrowed"
        DAMAGED = "D", "Damaged"
        LOST = "L", "Lost"

    book_id = models.ForeignKey("Book", on_delete=models.CASCADE)
    physical_status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.AVAILABLE
    )