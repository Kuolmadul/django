from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'class.html')

def about(request):
    return render(request,'about.html')

def details(request):
    return render(request,'Details.html')