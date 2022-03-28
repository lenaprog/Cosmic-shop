from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class Article (models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=64, decimal_places=2)
    image_link = models.CharField(max_length=200, default=None, blank=True, null=True)

   