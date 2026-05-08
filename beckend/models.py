from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    contact=models.CharField(max_length=40)
    marks=models.IntegerField()
    email=models.EmailField(unique=True)