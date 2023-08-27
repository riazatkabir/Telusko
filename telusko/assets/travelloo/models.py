from django.db import models

# Create your models here.

class Destination(models.Model):
  name = models.CharField()
  desc = models.CharField()
  img = models.ImageField(upload_to='pics')
  price = models.IntegerField()
  offer = models.BooleanField(default=False)


    