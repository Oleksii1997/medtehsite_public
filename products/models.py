from django.db import models

# Create your models here.

#Createing status the products
class StatusGoods(models.Model):
	status = models.CharField(max_length=24, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.status

	class Meta:
		verbose_name = "Статус товару: "
		verbose_name_plural = "Статуси товарів"

#Creating section category the products (category_products)
class SectionCategoryGoods(models.Model):
	section_category = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	sections_category_image = models.ImageField(upload_to='stylesheet/media/section_category_products_image/', default = 0)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.section_category

	class Meta:
		verbose_name = "Розділ категорії товару "
		verbose_name_plural = "Розділ категорій товарів"

#Creating category the products (sub category products)
class CategoryGoods(models.Model):
	category = models.CharField(max_length=64, blank=True, null=True, default=None)
	section_category = models.ForeignKey(SectionCategoryGoods, on_delete=models.CASCADE, default=1)
	is_active = models.BooleanField(default=True)
	category_image = models.ImageField(upload_to='stylesheet/media/category_product_image/', default = 0)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.category

	class Meta:
		verbose_name = "Категорія товару: "
		verbose_name_plural = "Категорії товарів"

#Creating brand products models
class BrandProducts(models.Model):
	brand_name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.brand_name

	class Meta:
		verbose_name = "Виробник товару: "
		verbose_name_plural = "Виробники товарів"

#create products
class Product(models.Model):
	product_category = models.ForeignKey(CategoryGoods, on_delete=models.CASCADE, default=0)
	product_name = models.CharField(max_length=64)
	is_active = models.BooleanField(default=True)
	compatible_product_brand = models.ManyToManyField(BrandProducts)
	description = models.TextField(blank=True, null=True, default=None)
	technical_characteristic = models.TextField(blank=True, null=True, default=None)
	status_product = models.ForeignKey(StatusGoods, on_delete=models.CASCADE, default=0)
	product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	product_discount = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Товари %s %s" % (self.product_name, self.status_product.status)

	def get_brand(self):#для того, щоб відобразити в адмінці поле ManyToManyField
		return "%s"%(", ".join([brand.brand_name for brand in self.compatible_product_brand.all()]))
		get_brand.short_description = 'Product'

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товари"

#create database for images the products
class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
	#link upload image relatively root folder the project
	image = models.ImageField(upload_to='stylesheet/media/product_images/')
	#for turn off/on active products or thome other things
	is_active = models.BooleanField(default=True)
	#for visualation main image item products
	is_main_image = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Фото товару %s" % self.product.product_name

	class Meta:
		verbose_name = "Фото"
		verbose_name_plural = "Фото товарів"

#this is model for homepage content
class HeaderCarousel(models.Model):
	image = models.ImageField(upload_to='stylesheet/media/homepage_carousel/')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Фото головної каруселі" 

	class Meta:
		verbose_name = "Фото каруселі"
		verbose_name_plural = "Фото каруселі"