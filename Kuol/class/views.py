from django.shortcuts import render
from django.http import HttpResponse
from . models import Student, Dormitory

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {"students": students})

def dormitory(request):
    dormitories = Dormitory.objects.all()
    return render(request, 'dormitories.html', {"dormitory": dormitories})

def insert_students(request):
    return render(request,'insertstudents.html')