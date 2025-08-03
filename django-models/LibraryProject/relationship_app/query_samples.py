from relationship_app.models import Author, Book, Library, Librarian


# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# 2️⃣ List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3️⃣ Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)


# Example usage (for testing inside Django shell)
"""
from relationship_app.query_samples import books_by_author, books_in_library, librarian_for_library

print(books_by_author("John Doe"))
print(books_in_library("Central Library"))
print(librarian_for_library("Central Library"))
"""
