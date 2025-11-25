from django.urls import path
from . import views

urlpatterns = [
    path("add_book/", views.add_book_view, name="add_book"),
    path("edit_book/", views.change_book_view, name="edit_book"),
    path("delete_book/", views.delete_book_view, name="delete_book"),
]
