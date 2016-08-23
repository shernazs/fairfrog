from django.shortcuts import render
from django.http import HttpResponse
import json
from shop.models import CrawledProducts
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
    return HttpResponse("FairFrog says hey there world!")


def get_products(request):
	logger = set_log()
    response = {'status': 0}
    try:
        products_list = []
        products = CrawledProducts.objects.all()
        for product in products:
            temp_product = {}
            temp_product['id'] = product.product_id
            temp_product['title'] = product.title
            temp_product['webshop_name'] = product.webshop_name
            temp_product['webshop_logo'] = product.webshop_logo
            temp_product['url'] = product.url
            temp_product['image'] = product.image
            temp_product['price'] = product.price
            temp_product['discount_price'] = product.discount_price
            temp_product['brand'] = product.brand
            temp_product['sizes'] = product.sizes
            temp_product['product_cat'] = product.product_cat
            temp_product['style'] = product.style
            temp_product['description'] = product.description
            products_list.append(temp_product)

        response['products_list'] = products_list
        response['status'] = 1
    except:
        #print("ERROR")
        logger.error(" ", exc_info=True, extra={'request': request})
    return HttpResponse(json.dumps(response), content_type='application/json')

