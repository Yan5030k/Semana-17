from django.shortcuts import render, redirect
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


# ========== VISTAS PARA AUTOR ==========

def author_list(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/author_list.html', {'autores': autores})


def author_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # nombre del path en urls
    else:
        form = AutorForm()
    return render(request, 'biblioteca/author_form.html', {'form': form})


# ========== VISTAS PARA LIBRO ==========

def book_list(request):
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'biblioteca/book_list.html', {'libros': libros})


def book_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/book_form.html', {'form': form})
