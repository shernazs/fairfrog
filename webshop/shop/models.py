from __future__ import unicode_literals

from django.db import models

# Create your models here.
# id INTEGER PRIMARY KEY, Webshop VARCHAR(50), Title VARCHAR(100), Description TEXT, Url VARCHAR(2000), \
# Image VARCHAR(2000), Logo VARCHAR(2000), Style VARCHAR(3), Brand VARCHAR(100), Price DOUBLE, Discount_price DOUBLE,\
# Sizes TEXT, Categories TEXT, Hashtags 

class Products(models.Model):
	Id = models.IntegerField(primary_key=True, unique=True, null=False)
	Webshop = models.CharField(max_length=20)
	Title = models.CharField(max_length=100)
	Url = models.CharField(max_length=200)
	Image = models.CharField(max_length=2000, default=None, blank=True, null=True)
	Logo = models.CharField(max_length=2000)
	Webshop_Url = models.CharField(max_length=100)
	Brand = models.CharField(max_length=100, default=None, blank=True, null=True)
	Price = models.FloatField()
	Discount_price = models.FloatField()
	Sizes = models.CharField(max_length=20)
	Description = models.TextField()
	Categories = models.CharField(max_length=100)
	Hashtags = models.TextField()

	class Meta:
		db_table = "Products"


class Popular_Products(models.Model):
	Id = models.IntegerField(primary_key=True, unique=True, default=1)
	Product_Id = models.CharField(max_length=5)

	class Meta:
		db_table = "Popular_Products"


class Featured_Products(models.Model):
	Id = models.IntegerField(primary_key=True, unique=True, default=1)
	Product_Id = models.CharField(max_length=5)

	class Meta:
		db_table = "Advertorial_Products"
