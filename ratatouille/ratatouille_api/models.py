# from django.db import models
from djongo import models

# Create your models here.
# class Product(models.Model): 
#     _id = models.ObjectIdField()
#     name = models.TextField(max_length= 255, null=False, blank=False)

    # def __str__(self):
    #     return self.name


# Create your models here.
class Product(models.Model): 
    _id = models.ObjectIdField()
    name = models.TextField(max_length= 255, null=False, blank=False)
    link = models.TextField(max_length= 255, null=False, blank=False)
    price = models.FloatField(default=[])
    users = models.JSONField(default=[])
    ingredients = models.JSONField(default=[])
    store = models.JSONField(default=[])
    categories = models.JSONField(default=[])

    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField()
    firstname = models.TextField(max_length= 255, null=False, blank=False)
    lastname = models.TextField(max_length= 255, null=False, blank=False)
    email = models.EmailField(max_length= 255, null=False, blank=False)
    password = models.TextField(max_length= 255, null=False, blank=False)

    def __str__(self):
        return self.firstname

class Menu(models.Model):
    _id = models.ObjectIdField()
    name = models.TextField(max_length= 255, null=False, blank=False)
    dishes = models.JSONField(default=[])

    def __str__(self):
        return self.name