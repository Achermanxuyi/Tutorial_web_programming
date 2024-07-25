from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Hello/index.html")

def Iris(request):
    return HttpResponse("Hello Iris!")

def Kaori(request):
    return HttpResponse("Hello Kaori!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
