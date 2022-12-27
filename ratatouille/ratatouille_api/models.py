# from django.db import models
from djongo import models

# Create your models here.
class Product(models.Model): 
    _id = models.ObjectIdField()
    name = models.TextField(max_length= 255, null=False, blank=False)
