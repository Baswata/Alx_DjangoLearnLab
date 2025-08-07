from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# ----------------------
# Author Model
# ----------------------
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ----------------------
# Book Model (ForeignKey to Author)
# ----------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change book details"),
            ("can_delete_book", "Can delete a book"),
        ]


# ----------------------
# Library Model (ManyToMany to Book)
# ----------------------
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# ----------------------
# Librarian Model (OneToOne to Library)
# ----------------------
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# ----------------------
# UserProfile Model for Role-Based Access Control
# ----------------------
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# ----------------------
# Signal to create/update UserProfile automatically
# ----------------------
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # default='Member'
    else:
        instance.userprofile.save()
