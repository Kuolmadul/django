from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('location/', views.location)
]



