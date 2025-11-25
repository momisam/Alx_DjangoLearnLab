from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

"""
BOOK CRUD VIEWS USING DJANGO REST FRAMEWORK GENERIC VIEWS
----------------------------------------------------------
These views implement:

- List all books (GET)
- Retrieve single book (GET)
- Create book (POST)
- Update book (PUT/PATCH)
- Delete book (DELETE)

Permissions:
- List + Detail: AllowAny
- Create, Update, Delete: Authenticated users only
"""

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
