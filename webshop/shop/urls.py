__author__ = 'shalu'
from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_products', views.get_products, name='get_products'),
    url(r'^get_popular_products', views.get_popular_products, name='get_popular_products'),
    url(r'^get_featured_products', views.get_featured_products, name='get_featured_products'),

]

