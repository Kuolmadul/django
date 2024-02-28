from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('student/',views.student),
    path('dormitory/',views.dormitory),
    path('insertstudent/',views.insert_students)

    ]