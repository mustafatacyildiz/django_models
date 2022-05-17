from email import charset
from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
