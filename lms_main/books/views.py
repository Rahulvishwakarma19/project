from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"books/home.html")
    # return HttpResponse("home page..")

def books(request):
    details = {'name': 'Complete Python Course', 'author' : 'Rahul', 'publisher' : 'Rahul'}
    return render(request,"books/books.html", context=details)
    # return HttpResponse("books page ..")