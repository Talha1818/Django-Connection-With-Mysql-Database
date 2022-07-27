from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
