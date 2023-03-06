from django.urls import path

from e_book_app.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboult/', views.about_page, name='about_page'),
    path('catalogue/', views.catalogue, name='catalogue'),

]