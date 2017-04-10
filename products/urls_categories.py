from django.conf.urls import url, include
from django.contrib import admin
from . import views

from .views import CategoryListView, CategoryDetailView

urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='category_list'),
	url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
]
