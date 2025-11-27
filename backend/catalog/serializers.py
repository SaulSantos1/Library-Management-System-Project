from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ['created_at', 'updated_at']