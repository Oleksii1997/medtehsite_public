from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget



# Register your models here.
#for show the image in the administrator page or another page
class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0

class StatusGoodsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusGoods._meta.fields]

	class Meta:
		model = StatusGoods

admin.site.register(StatusGoods, StatusGoodsAdmin)

class SectionCategoryGoodsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in SectionCategoryGoods._meta.fields]

	class Meta:
		model = SectionCategoryGoods

admin.site.register(SectionCategoryGoods, SectionCategoryGoodsAdmin)

class CategoryGoodsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in CategoryGoods._meta.fields]

	class Meta:
		model = CategoryGoods

admin.site.register(CategoryGoods, CategoryGoodsAdmin)

class BrandProductsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in BrandProducts._meta.fields]

	class Meta:
		model = BrandProducts

admin.site.register(BrandProducts, BrandProductsAdmin)


#клас ProducrResource для реалізації import-export data products in database 
class ProductResource(resources.ModelResource):
	id = fields.Field(attribute='id', column_name='Id товару')
	product_category = fields.Field(column_name='Категорія товарів', attribute='product_category', widget=ForeignKeyWidget(CategoryGoods, 'category'))
	product_name = fields.Field(attribute='product_name', column_name='Назва товару')
	is_active = fields.Field(attribute='is_active', column_name='Товар активний/неактивний (True/False)')
	compatible_product_brand = fields.Field(attribute='compatible_product_brand', column_name='Бренди сумісності',widget=ManyToManyWidget(BrandProducts))
	description = fields.Field(attribute='description', column_name='Опис товару')
	technical_characteristic = fields.Field(attribute='technical_characteristic', column_name='Технічна характеристика')
	status_product = fields.Field(column_name='Статус товару', attribute='status_product', widget=ForeignKeyWidget(StatusGoods, 'status'))
	product_price = fields.Field(attribute='product_price', column_name='Ціна, Грн')
	product_discount = fields.Field(attribute='product_discount', column_name='Знижка, %')
	created = fields.Field(attribute='created', column_name='Дата створення')
	updated = fields.Field(attribute='updated', column_name='Дата оновлення')

	class Meta:
		model = Product

class ProductAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    resource_class=ProductResource
    summernote_fields = ('description', 'technical_characteristic')
    list_display = ['id','product_category','product_name','is_active', 'get_brand', 'status_product', 'product_price', 'product_discount', 'created', 'updated']
    inlines = [ProductImageInline]

    class Meta:
    	model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]

	class Meta:
		model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)


class HeaderCarouselAdmin(admin.ModelAdmin):
	list_display = [field.name for field in HeaderCarousel._meta.fields]

	class Meta:
		model = HeaderCarousel

admin.site.register(HeaderCarousel, HeaderCarouselAdmin)
