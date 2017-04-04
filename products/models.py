from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self.db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()



class Product (models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places= 2, max_digits=20)
	active = models.BooleanField(default=True)
	#slug
	# inventory?

	objects = ProductManager()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})

class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places= 2, max_digits=20)
	sale_price = models.DecimalField(decimal_places= 2, max_digits=20, null=True, blank=True)
	active = models.BooleanField(default=True)
	inventory = models.IntegerField(null=True, blank=True) #refers to unlimited amount

	def __unicode__(self):
		return self.title

	def get_price(self):
		if self.sale_price is not None:
			return self.sale_price
		else:
			return self.price

	def get_absolute_url(self):
		return self.product.get_absolute_url()

def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
	product = instance
	variations = product.variation_set.all()
	if variations.count() ==0:
		new_variation = Variation()
		new_variation.product = product
		new_variation.title = product.title
		new_variation.price = product.price
		new_variation.save()

post_save.connect(product_post_saved_receiver, sender=Product)


#Product Images

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/img/')

	def __unicode__(self):
		return self.product.title



#Product Category




