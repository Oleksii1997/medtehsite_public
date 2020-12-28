from django.contrib import admin
from .models import *

# Register your models here.
class TypeDeviceAdmin(admin.ModelAdmin):
	list_display = [field.name for field in TypeDevice._meta.fields]

	class Meta:
		model = TypeDevice

admin.site.register(TypeDevice, TypeDeviceAdmin)

class ModelDeviceAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ModelDevice._meta.fields]

	class Meta:
		model = ModelDevice

admin.site.register(ModelDevice, ModelDeviceAdmin)

class RepairStatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RepairStatus._meta.fields]

	class Meta:
		model = RepairStatus

admin.site.register(RepairStatus, RepairStatusAdmin)

class PayRepairStatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in PayRepairStatus._meta.fields]

	class Meta:
		model = PayRepairStatus

admin.site.register(PayRepairStatus, PayRepairStatusAdmin)

class DeliveryMethodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in DeliveryMethod._meta.fields]

	class Meta:
		model = DeliveryMethod

admin.site.register(DeliveryMethod, DeliveryMethodAdmin)

class WarrantyPeriodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in WarrantyPeriod._meta.fields]

	class Meta:
		model = WarrantyPeriod

admin.site.register(WarrantyPeriod, WarrantyPeriodAdmin)

class WarrantyStatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in WarrantyStatus._meta.fields]

	class Meta:
		model = WarrantyStatus

admin.site.register(WarrantyStatus, WarrantyStatusAdmin)

class RepairClientAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RepairClient._meta.fields]

	class Meta:
		model = RepairClient

admin.site.register(RepairClient, RepairClientAdmin)

class RepairDeviceAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RepairDevice._meta.fields]

	class Meta:
		model = RepairDevice

admin.site.register(RepairDevice, RepairDeviceAdmin)