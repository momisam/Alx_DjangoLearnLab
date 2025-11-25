from rest_framework import generics, permissions
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

# -----------------------------------------------
# LIST VIEW — GET /books/
# -----------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------------------------
# DETAIL VIEW — GET /books/<id>/
# -----------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------------------------
# CREATE VIEW — POST /books/create/
# -----------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Automatically assign authenticated user's ID as context if needed
    def perform_create(self, serializer):
        serializer.save()


# -----------------------------------------------
# UPDATE VIEW — PUT/PATCH /books/<id>/update/
# -----------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# -----------------------------------------------
# DELETE VIEW — DELETE /books/<id>/delete/
# -----------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
