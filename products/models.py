from django.db import models

# Create your models here.
class LiveProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='img')
    offer =models.BooleanField(default=False)
    price  = models.FloatField()




class  FrozonProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='img')
    offer =models.BooleanField(default=False)
    price  = models.FloatField()

class BreedProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='img')
    offer =models.BooleanField(default=False)
    price  = models.FloatField()

