from django.db import models

# Create your models here.
class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    position = models.CharField(max_length=50)

    experience = models.IntegerField()
