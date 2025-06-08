from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Products(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
