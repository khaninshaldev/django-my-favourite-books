from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = { "books": all_books }
    return render(request, 'main/index.html', context)

def newBook(request):
    if request.POST:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('/')


    context = { 'book_form': BookForm }
    return render(request, 'main/new_book.html', context)    


def editBook(request, id):
    selected_book = Book.objects.get(id=id)
    book_form = BookForm(instance=selected_book)

    if request.POST:
        book_form = BookForm(request.POST, instance=selected_book)
        if book_form.is_valid():
            book_form.save()
            return redirect('/')

    context = { 'book_form': book_form }
    return render(request, 'main/edit_book.html', context)   

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')