from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/read/<int:pk>/', views.book_read, name='book_read'),  # Add this path
]
