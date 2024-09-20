from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    #return render(request, 'store/home.html'))
    return HttpResponse("<h1>hello this is Home Page</h1>")
