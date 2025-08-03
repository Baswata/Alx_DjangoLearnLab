from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Registration view (custom)
    path('register/', register_view, name='register'),

    # Login view (built-in, required by ALX)
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view (built-in, required by ALX)
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
