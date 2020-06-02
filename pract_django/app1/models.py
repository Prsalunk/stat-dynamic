from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    offr = models.BooleanField(default=False)