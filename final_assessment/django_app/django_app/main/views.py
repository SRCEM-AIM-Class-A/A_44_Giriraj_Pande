from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/home.html', {'books': books, 'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home') 