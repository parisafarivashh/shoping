from django.db import models

class Fruit(models.Model):
  name = models.CharField(max_length=50)
  price = models.FloatField()
  stock = models.IntegerField()
  image_url = models.CharField(max_length=2083)

class Offer(models.Model):
  code = models.CharField(max_length=25)
  description = models.CharField(max_length=60)
  discount = models.FloatField()
  
