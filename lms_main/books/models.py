from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    edition = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    
