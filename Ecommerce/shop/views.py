from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Home page")


def about(request):
    return HttpResponse("About page")


def Contact(request):
    return HttpResponse("Contact")


def store(request):
    return HttpResponse("Our store")


def show(request):
    return HttpResponse("Show page")
