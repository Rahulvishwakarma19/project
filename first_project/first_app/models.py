from django.db import models

# Create your models here.

class Students(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=128)
    age = models.IntegerField()

    def __str__(self):
        return self.name