from django.shortcuts import render, redirect

from e_book_app.books.forms import BookForm
from e_book_app.books.models import Book


# Create your views here.


def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {'form': form}
    return render(request, 'books/add-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }

    return render(request, 'books/book-details.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book, initial=book.__dict__)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }

    return render(request, 'books/edit-book.html', context)
