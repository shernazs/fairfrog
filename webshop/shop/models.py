from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CrawledProducts(models.Model):
    product_id = models.IntegerField()
    webshop_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2000)
    image = models.CharField(max_length=2000)
	webshop_logo = models.CharField(max_length=2000)
    brand = models.CharField(max_length=100, default=None, blank=True, null=True)
    price = models.FloatField()
	discount_price = models.FloatField()
    sizes = models.TextField()
	description = models.TextField()
	product_cat = models.TextField()
	style = models.CharField(max_length=3)
