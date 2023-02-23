from django.contrib import admin

from e_book_app.accounts.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_users = ("name", "email")
