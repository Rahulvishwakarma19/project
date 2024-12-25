from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=64)
    details = models.CharField(max_length=1024)