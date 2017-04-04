from django.conf.urls import url, include
from django.contrib import admin
from . import views

from .views import ProductDetailView, ProductListView

urlpatterns = [
	# url(r'^$', views.home, name='home'),
	url(r'^$', ProductListView.as_view(), name='product_list'),
	url(r'^(?P<pk>\d+)', ProductDetailView.as_view() , name='product_detail'),

]
