from django.urls import path
from . import views

urlpatterns = [
    # Home -> que la raíz muestre la lista de autores
    path('', views.author_list, name='home'),

    # Autores
    path('autores/', views.author_list, name='author_list'),
    path('autores/nuevo/', views.author_create, name='author_create'),

    # Libros
    path('libros/', views.book_list, name='book_list'),
    path('libros/nuevo/', views.book_create, name='book_create'),
]
