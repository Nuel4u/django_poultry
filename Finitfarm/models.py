from django.db import models

# Create your models here.
class Destination(models.Model):

    
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price  = models.FloatField()
    offer = models.BooleanField(default=False)


class Frozen(models.Model):
    name = models.CharField(max_length=255) 
    des =models.TextField()   
    img = models.ImageField(upload_to='img')

