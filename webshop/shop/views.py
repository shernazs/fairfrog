from django.shortcuts import render
from django.http import HttpResponse
import json
from shop.models import Products, Popular_Products, Featured_Products
import logging
from datetime import datetime


def set_log():
	logfile = '/home/fairfrog/Logs/api_log_' + datetime.today().strftime('%y-%m-%d') + '.log'
	logger = logging.getLogger('api_setup')
	handler = logging.FileHandler(logfile, mode='a')
	formatter = logging.Formatter('%(asctime)s\t[%(levelname)s]\t%(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler) 
	logger.setLevel(logging.DEBUG)
	return logger


def index(request):
	return HttpResponse("FairFrog says: Hey there, world!")


def get_featured_products(request):
	logger = set_log()
	response = {'status': 0}
	product_ids = Featured_Products.objects.all()
	products_list = []
	try:
		for product_id in product_ids:
			temp_product = {}
			product = Products.objects.get(Id=product_id.Product_Id)
			temp_product['Id'] = product.Id
			temp_product['title'] = product.Title
			temp_product['webshop_name'] = product.Webshop
			temp_product['webshop_logo'] = product.Logo
			temp_product['webshop_url'] = product.Webshop_Url
			temp_product['url'] = product.Url
			temp_product['image'] = product.Image
			temp_product['price'] = product.Price
			temp_product['discount_price'] = product.Discount_price
			temp_product['brand'] = product.Brand
			temp_product['sizes'] = product.Sizes.split('|')
			temp_product['categories'] = product.Categories.lower().split('|')
			temp_product['hashtags'] = product.Hashtags
			temp_product['description'] = product.Description
			products_list.append(temp_product)
	except Exception as e:
		logger.error(e, exc_info=True, extra={'request': request})

	response['featured_products_list'] = products_list
	response['status'] = 1
	return HttpResponse(json.dumps(response), content_type='application/json')


def get_popular_products(request):
	logger = set_log()
	response = {'status': 0}
	product_ids = Popular_Products.objects.all()
	products_list = []
	try:
		for product_id in product_ids:
			temp_product = {}
			product = Products.objects.get(Id=product_id.Product_Id)
			temp_product['Id'] = product.Id
			temp_product['title'] = product.Title
			temp_product['webshop_name'] = product.Webshop
			temp_product['webshop_logo'] = product.Logo
			temp_product['webshop_url'] = product.Webshop_Url
			temp_product['url'] = product.Url
			temp_product['image'] = product.Image
			temp_product['price'] = product.Price
			temp_product['discount_price'] = product.Discount_price
			temp_product['brand'] = product.Brand
			temp_product['sizes'] = product.Sizes.split('|')
			temp_product['categories'] = product.Categories.lower().split('|')
			temp_product['hashtags'] = product.Hashtags
			temp_product['description'] = product.Description
			products_list.append(temp_product)
	except Exception as e:
		logger.error(e, exc_info=True, extra={'request': request})

	response['popular_products_list'] = products_list
	response['status'] = 1
	return HttpResponse(json.dumps(response), content_type='application/json')


def get_products(request):
	logger = set_log()
	response = {'status': 0}
	cat = request.GET.get('cat', '')
	products_list = []
	if cat != '':
		subcat = request.GET.get('subcat', '')
		products = Products.objects.all().filter(Categories__contains=cat.lower()).filter(Categories__contains=subcat.lower())
	else:
		products = Products.objects.all()
    
	try:
		for product in products:
			temp_product = {}
			temp_product['Id'] = product.Id
			temp_product['title'] = product.Title
			temp_product['webshop_name'] = product.Webshop
			temp_product['webshop_logo'] = product.Logo
			temp_product['webshop_url'] = product.Webshop_Url
			temp_product['url'] = product.Url
			temp_product['image'] = product.Image
			temp_product['price'] = product.Price
			temp_product['discount_price'] = product.Discount_price
			temp_product['brand'] = product.Brand
			temp_product['sizes'] = product.Sizes.split('|')
			temp_product['categories'] = product.Categories.lower().split('|')
			temp_product['hashtags'] = product.Hashtags
			temp_product['description'] = product.Description
			products_list.append(temp_product)
	except Exception as e:
		logger.error(e, exc_info=True, extra={'request': request})
    
	response['products_list'] = products_list
	response['status'] = 1
	return HttpResponse(json.dumps(response), content_type='application/json')

