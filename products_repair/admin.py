from django.contrib import admin
from .models import *

# Register your models here.
class ProductsRepairCategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductsRepairCategory._meta.fields]

	class Meta:
		model = ProductsRepairCategory

admin.site.register(ProductsRepairCategory, ProductsRepairCategoryAdmin)

class RepairedProductsImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RepairedProductsImage._meta.fields]

	class Meta:
		model = RepairedProductsImage

admin.site.register(RepairedProductsImage, RepairedProductsImageAdmin)

class RepairWorkDescriptionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RepairWorkDescription._meta.fields]

	class Meta:
		model = RepairWorkDescription

admin.site.register(RepairWorkDescription, RepairWorkDescriptionAdmin)