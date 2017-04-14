from django.contrib import admin

# Register your models here.
from .models import Product, Variation, ProductImage, Category, CategoryImage, ProductFeatured


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'price']
	inlines =[
		ProductImageInline,
		VariationInline
	]
	class Meta:
		model = Product


class CategoryImageInline(admin.TabularInline):
	model = CategoryImage
	extra = 0


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines =[
		CategoryImageInline,
	]
	class Meta:
		model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductFeatured)




