from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('e_book_app.core.urls')),
    path('book/', include('e_book_app.books.urls')),
    path('account/', include('e_book_app.accounts.urls')),
]
