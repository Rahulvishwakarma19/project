from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Students

# Create your views here.
def index(request):
    data = Students.objects.all()
    records = {'Student_data': data}
    return render(request,"first_app/index_bootstrap.html", context=records)

def welcome(request):
    # return HttpResponse("WELCOME DJANGO")
    return render(request,"home.html")