from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    details = {"name" : "Rahul", "age" : 21}
    return render(request,"first_app/index.html", context=details)

def welcome(request):
    # return HttpResponse("WELCOME DJANGO")
    return render(request,"home.html")