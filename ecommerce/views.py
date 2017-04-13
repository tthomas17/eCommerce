from django.shortcuts import render

from products.models import ProductFeatured
from products.models import Category

def home(request):
	featured_image = ProductFeatured.objects.first()
	categories_list = Category.objects.all()

	context = {
		"featured_image": featured_image,
		"categories_list": categories_list
	}
	return render(request, "home.html", context)