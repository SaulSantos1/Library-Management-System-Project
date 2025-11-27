from rest_framework import viewsets, permissions
from .permissions import IsProfileLibrarian
from .serializers import BookSerializers
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers

    def get_queryset(self):
        queryset = Book.objects.all().order_by('id')

        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        isbn = self.request.query_params.get('isbn')
        gender = self.request.query_params.get('gender')
        publisher = self.request.query_params.get('publisher')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn)
        if gender:
            queryset = queryset.filter(gender__icontains=gender)
        if publisher:
            queryset = queryset.filter(publisher__name__icontains=publisher)

        return queryset

    def get_permissions(self):
        """
        Define permissões dinamicamente baseadas na ação.
        """
        if self.action == 'destroy':
            permission_classes = [IsProfileLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
        
        return [permission() for permission in permission_classes]