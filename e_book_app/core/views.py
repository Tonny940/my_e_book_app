from django.shortcuts import render

from e_book_app.books.models import Book


# Create your views here.
def index(request):
    return render(request, 'core/home-page.html')


def about_page(request):
    return render(request, 'core/about-page.html')


def catalogue(request):
    all_books = Book.objects.all()

    context = {
        'all_books': all_books,
    }
    return render(request, 'core/catalogue.html', context)
