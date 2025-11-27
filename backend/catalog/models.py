from django.db import models


class Book(models.Model):

    isbn = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.ForeignKey(
        "Publisher", on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    keywords = models.CharField(max_length=150)
    sinopse = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


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


class Publisher(models.Model):

    name = models.CharField(max_length=150, unique=True)
    site = models.URLField(null=True, blank=True)
    phone_contact = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
