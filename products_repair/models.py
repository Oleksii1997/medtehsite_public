from django.db import models

#create device in repair
class ProductsRepairCategory(models.Model):
	product_category_name = models.CharField(max_length=128)
	category_image = models.ImageField(upload_to='stylesheet/media/category_repair_image/', default = 0)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Категорія %s " % (self.product_category_name)

	class Meta:
		verbose_name = "Категорії ремонту"
		verbose_name_plural = "Категорії ремонтів"

#model for repaired products
class RepairedProductsImage(models.Model):
	category = models.ForeignKey(ProductsRepairCategory, on_delete=models.CASCADE, default=0)
	category_image = models.ImageField(upload_to='stylesheet/media/repaired_products_image/', default = 0)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Фото %s " % (self.category.product_category_name)

	class Meta:
		verbose_name = "Фото відремонтованого приладу"
		verbose_name_plural = "Фото відремонтованих приладів"

#model for description malfunction
class RepairWorkDescription(models.Model):
	category = models.ForeignKey(ProductsRepairCategory, on_delete=models.CASCADE, default=0)
	malfunction_descript = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Опис несправності %s " % (self.category.product_category_name)

	class Meta:
		verbose_name = "Опис несправності та роботи"
		verbose_name_plural = "Описи несправностей та робіт"


