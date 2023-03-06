from django.urls import path

from e_book_app.books import views

urlpatterns = [
    path('add/', views.add_book, name='add-new-book'),
    path('<int:pk>/', views.book_details, name='book_details'),
    path('<int:pk>/edit/', views.edit_book, name='edit-book')
]
