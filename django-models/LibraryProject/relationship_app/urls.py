from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register_view

urlpatterns = [
    # Books and library views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # User registration (custom)
    path('register/', register_view, name='register'),

    # Built-in authentication views (required for ALX checks)
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
