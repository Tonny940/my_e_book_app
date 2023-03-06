from django import forms

from e_book_app.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Book Author'}),
            'date_of_publishing': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'book_photo': forms.TextInput(attrs={'placeholder': 'Link to image'})
        }
        labels = {
            'title': 'Book Title',
            'author': 'Book Author',
        }
