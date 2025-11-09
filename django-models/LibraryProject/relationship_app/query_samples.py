# relationship_app/query_samples.py
"""
Run these snippets from Django shell or call them inside a management command.
Examples show how to execute the required queries.
"""

from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return []
    return list(author.books.all())

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return []
    return list(library.books.all())

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    # since Librarian is OneToOne on Library, you can use related name 'librarian'
    return getattr(library, 'librarian', None)

# Example usage:
if __name__ == "__main__":
    print("Books by Chinua Achebe:", [b.title for b in books_by_author('Chinua Achebe')])
    print("Books in Lagos Central Library:", [b.title for b in books_in_library('Lagos Central Library')])
    lib_librarian = librarian_for_library('Lagos Central Library')
    print("Librarian:", lib_librarian.name if lib_librarian else 'None')
