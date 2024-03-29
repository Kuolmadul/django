from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    idCard = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    number = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


