from django.urls import path
from . import views

urlpatterns = [
    path('book-list/', views.book_list, name='book-list'),
    path('view-book/', views.view_book, name='view-book'),
    path('create-book/', views.create_book, name='create-book'),
    path('edit-book/', views.edit_book, name='edit-book'),
    path('delete-book/', views.delete_book, name='delete-book'),
]
