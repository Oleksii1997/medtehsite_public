from django.db import models
from products.models import Product
from django.db.models.signals import post_save

		

#this is status the orders
class Status(models.Model):
	status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.status_name

	class Meta:
		verbose_name = "Статус"
		verbose_name_plural = "Статуси замовлень"


# creating orders database
class Order(models.Model):
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price all products in the order
	custumer_name = models.CharField(max_length=64)
	custumer_fathername = models.CharField(max_length=64, default=0)
	custumer_surname = models.CharField(max_length=64, default=0)
	custumer_email = models.EmailField()
	custumer_phone = models.CharField(max_length=32)
	how_shipping = models.CharField(max_length=128)
	shipping_address = models.CharField(max_length=256)
	coment_to_order = models.TextField(blank=True, null=True, default=None)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Замовлення %s %s" % (self.id, self.status.status_name)

	class Meta:
		verbose_name = "Замовлення"
		verbose_name_plural = "Всі Замовлення"

#creating database for products in orders

class ProductInOrder(models.Model):
	#creating link on databases for order and product
	order = models.ForeignKey(Order,  on_delete=models.CASCADE, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	number = models.IntegerField(default=1)
	product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#number*product_price
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return "Товари в замовленні %s" % self.product.product_name #output name products in orders

	class Meta:
		verbose_name = "Замовлений товар"
		verbose_name_plural = "Товари в замовленні"
    
    #override method some arguments or fields
	def save(self, *args, **kwargs):
		product_price = self.product.product_price
		self.product_price = product_price
		self.total_price = self.number * product_price

		super(ProductInOrder, self).save(*args, **kwargs)

#post save method for calculate total price in the order
def product_in_order_post_seve(sender, instance, created, **kwargs):
	order = instance.order
	all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

	order_total_price = 0
	for item in all_products_in_order:
		order_total_price += item.total_price
		
	instance.order.total_price = order_total_price
	instance.order.save(force_update=True)
post_save.connect(product_in_order_post_seve,sender=ProductInOrder)#we calling post save function

class ProductInBusket(models.Model):
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	order = models.ForeignKey(Order,  on_delete=models.CASCADE, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	number = models.IntegerField(default=1)
	product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#number*product_price
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return "Товари в замовленні %s" % self.product.product_name #output name products in orders

	class Meta:
		verbose_name = "Товари в корзині"
		verbose_name_plural = "Товари в корзинах"

	def save(self, *args, **kwargs):
		product_price = self.product.product_price-((self.product.product_price)*(self.product.product_discount)/100)#with discount
		self.product_price = product_price
		self.total_price = int(self.number) * product_price

		super(ProductInBusket, self).save(*args, **kwargs)