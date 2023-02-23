from django.urls import path

from e_book_app.books import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue')

]
