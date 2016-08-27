from __future__ import unicode_literals

from django.db import models

# Create your models here.
# id INTEGER PRIMARY KEY, Webshop VARCHAR(50), Title VARCHAR(100), Description TEXT, Url VARCHAR(2000), \
# Image VARCHAR(2000), Logo VARCHAR(2000), Style VARCHAR(3), Brand VARCHAR(100), Price DOUBLE, Discount_price DOUBLE,\
# Sizes TEXT, Categories TEXT, Hashtags 

class Products(models.Model):
	Id = models.IntegerField()
	Webshop = models.CharField(max_length=20)
	Title = models.CharField(max_length=100)
	Url = models.CharField(max_length=2000)
	Image = models.CharField(max_length=2000)
	Logo = models.CharField(max_length=2000)
	Brand = models.CharField(max_length=100, default=None, blank=True, null=True)
	Price = models.FloatField()
	Discount_price = models.FloatField()
	Sizes = models.TextField()
	Description = models.TextField()
	Categories = models.TextField()
	Hashtags = models.TextField()

	class Meta:
		db_table = "Products"
