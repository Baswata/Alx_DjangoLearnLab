from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # 
urlpatterns = [
    # Books and library views
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),  # ✅ secured add
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),  # ✅ secured edit
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),  # ✅ secured delete
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User registration
    path('register/', views.register, name='register'),  # ✅ now shows views.register

    # Role-based views
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),

    # Built-in authentication views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
