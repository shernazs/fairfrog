from django.shortcuts import render
from django.http import HttpResponse
import json
from shop.models import Products
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

def get_products(request):
	logger = set_log()
	response = {'status': 0}
        cat = request.GET.get('cat', '')
	try:
		products_list = []

                if cat != '':
                    products = Products.objects.all().filter(Categories__contains=cat)
                else:
		    products = Products.objects.all()


		for product in products:
			temp_product = {}
			temp_product['Id'] = product.Id
			temp_product['title'] = product.Title
			temp_product['webshop_name'] = product.Webshop
			temp_product['webshop_logo'] = product.Logo
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

		response['products_list'] = products_list
		response['status'] = 1
	except Exception as e:
		#print("ERROR")
		logger.error(e, exc_info=True, extra={'request': request})
	return HttpResponse(json.dumps(response), content_type='application/json')

