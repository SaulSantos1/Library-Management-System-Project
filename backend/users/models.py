from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = None
    last_name = None
    full_name = models.CharField(max_length=200)
    profile_type = models.ForeignKey(
        "ProfileType", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.full_name


class ProfileType(models.Model):

    class Type(models.TextChoices):
        STUDENT = "S", "Student"
        TEACHER = "T", "Teacher"
        LIBRARIAN = "L", "Librarian"

    name = models.CharField(max_length=1, choices=Type.choices, default=Type.STUDENT)
    loan_days = models.PositiveSmallIntegerField()
