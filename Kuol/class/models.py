from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    # phone = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Dormitory(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.name