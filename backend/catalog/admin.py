from django.contrib import admin
from .models import Book, Copies, Publisher

admin.site.register(Book)
admin.site.register(Publisher)
