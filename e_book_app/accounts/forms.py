from django import forms

from e_book_app.accounts.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'name',
            'name',
            'name',

        ]