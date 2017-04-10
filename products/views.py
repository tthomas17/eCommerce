from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .forms import VariationInventoryFormSet
from .mixins import LoginRequiredMixin, StaffRequiredMixin
from .models import Product, Variation, Category

class CategoryListView(ListView):
	model = Category
	queryset= Category.objects.all()

class CategoryDetailView(DetailView):
	model = Category

	# def get_context_date(self, *args, **kwargs):
	# 	context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
	# 	obj = self.get_object()
	# 	product_set = obj.product_set.all()
	# 	default_products = obj.default_category.all()
	# 	products = (product_set | default_products).distinct()
	# 	context["products"] = products
	# 	return context



class VariationListView(StaffRequiredMixin, ListView):
	model = Variation
	queryset = Variation.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(VariationListView, self).get_context_data(*args, **kwargs)
		context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())

		return context

	def get_queryset(self, *args, **kwargs):
		product_pk = self.kwargs.get("pk")
		if product_pk:
			product = get_object_or_404(Product, pk=product_pk)
			queryset = Variation.objects.filter(product=product)
		return queryset
	def post(self, request, *args, **kwargs):

		formset = VariationInventoryFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				new_item = form.save(commit=False)
				product_pk = self.kwargs.get("pk")
				product = get_object_or_404(Product, pk=product_pk)
				new_item.product = product
				new_item.save()


			messages.success(request, "Inventory and Pricing has been updated")
			return redirect("product_list")
		raise Http404



class ProductListView(ListView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context["now"] = timezone.now()
		context["query"] = self.request.GET.get("q")
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)
				)
		return qs

class ProductDetailView(DetailView):
	model = Product
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		context['related'] = Product.objects.get_related(instance).order_by("?")[:5]
		return context








