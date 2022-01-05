from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField(default=None)
    roll = models.IntegerField(default=None)
    city = models.CharField(max_length=100)