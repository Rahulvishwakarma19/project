from django.urls import path
from books import views

urlpatterns = [
    path('',views.home,name='home'),
    path('books/',views.books,name='books'),
]