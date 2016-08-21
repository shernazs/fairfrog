from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CrawledProducts(models.Model):
    #id = models.IntegerField()
    webshop = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2000)
    img = models.CharField(max_length=2000)
    brand = models.CharField(max_length=100, default=None, blank=True, null=True)
    price = models.FloatField()
    sizes = models.TextField()
    tags = models.TextField()


