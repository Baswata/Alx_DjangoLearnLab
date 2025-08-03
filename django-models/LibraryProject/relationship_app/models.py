from django.db import models


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model (ForeignKey to Author)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Library Model (ManyToMany to Book)
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# Librarian Model (OneToOne to Library)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
