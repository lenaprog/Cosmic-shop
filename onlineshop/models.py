from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    pass

class Article (models.Model):
    title = models.CharField(max_length=64)
    short_description = models.TextField(default=None)
    description = models.TextField()
    details = models.TextField(default=None)
    price = models.DecimalField(max_digits=64, decimal_places=2)
    image_link = models.CharField(max_length=200, default=None, blank=True, null=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
