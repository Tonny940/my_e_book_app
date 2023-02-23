from django.urls import path, include

from e_book_app.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', include([
        path('details/', views.profile_details, name='profile-details')
    ]))
]