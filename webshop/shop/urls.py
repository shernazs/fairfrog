__author__ = 'shalu'
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', views.get_products, name='get_products'),

]

