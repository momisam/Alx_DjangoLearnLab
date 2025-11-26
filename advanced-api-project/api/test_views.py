"""
Test Suite for Django REST Framework API Views

This file contains:
- CRUD tests for the Book API endpoints
- Tests for filtering, searching, and ordering
- Tests for authentication and permission handling
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from .models import Author, Book


User = get_user_model()


class BookAPITests(APITestCase):
    """Tests for CRUD operations, filtering, searching, and ordering."""

    def setUp(self):
        # Create a user for authenticated operations
        self.user = User.objects.create_user(email="test@example.com", password="password123")

        # Create sample authors
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="Wole Soyinka")

        # Create books
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author1)
        self.book2 = Book.objects.create(title="The Lion and the Jewel", publication_year=1959, author=self.author2)

        self.client = APIClient()

    # -----------------------------
    # CRUD TESTS
    # -----------------------------

    def test_list_books(self):
        """Test retrieving all books."""
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book."""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book_authenticated(self):
        """Authenticated user should be able to create a book."""
        self.client.login(email="test@example.com", password="password123")
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users should not be able to create books."""
        url = reverse("book-create")
        data = {
            "title": "Fail Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Authenticated users should be able to update books."""
        self.client.login(email="test@example.com", password="password123")
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title", "publication_year": 1958, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        """Authenticated users should be able to delete books."""
        self.client.login(email="test@example.com", password="password123")
        url = reverse("book-delete", args=[this.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -----------------------------
    # FILTERING TESTS
    # -----------------------------

    def test_filter_by_title(self):
        url = reverse("book-list") + "?title=Things Fall Apart"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_filter_by_publication_year(self):
        url = reverse("book-list") + "?publication_year=1959"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1959)

    # -----------------------------
    # SEARCH TESTS
    # -----------------------------

    def test_search_by_title(self):
        url = reverse("book-list") + "?search=Lion"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # -----------------------------
    # ORDERING TESTS
    # -----------------------------

    def test_order_by_publication_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(
            response.data[0]["publication_year"],
            response.data[-1]["publication_year"]
        )
