from django.urls import path

from e_book_app.core import views

urlpatterns = [
    path('', views.about_page, name='about_page')
]