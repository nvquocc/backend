import string
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Tên", max_length=100)
    age = models.IntegerField("Tuổi")
    address = models.CharField("Địa chỉ", max_length=200)