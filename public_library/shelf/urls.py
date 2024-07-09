from django.urls import path
from . import views

urlpatterns = [
    path('', views.details_book, name='books'),
    path('authors/', views.details_author, name='authors'),
    path('details/<int:id>', views.details_book, name='detail_author'),
]