from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json

from shop.models import CrawledProducts
import logging

def index(request):
    return HttpResponse("FairFrog says hey there world!")

def get_products(request):
    response = {'status': 0}
    try:
        products_list = []
        products = CrawledProducts.objects.all()


        for product in products:
            temp_product = {}
            temp_product['id'] = product.id
            temp_product['title'] = product.title
            temp_product['url'] = product.url
            temp_product['img'] = product.img
            temp_product['price'] = product.price
            temp_product['brand'] = product.brand
            products_list.append(temp_product)
        response['products_list'] = products_list
        response['status'] = 1
    except:
        print("ERRORRRR")
        #logger.error(" ", exc_info=True, extra={'request': request})
    return HttpResponse(json.dumps(response), content_type='application/json')

