from django.db import models

#this is type device
class TypeDevice(models.Model):
	device_type = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.device_type

	class Meta:
		verbose_name = "Тип приладу"
		verbose_name_plural = "Типи приладів"

#this is model device
class ModelDevice(models.Model):
	device_model = models.CharField(max_length=64, blank=True, null=True, default=None)
	type_device = models.ForeignKey(TypeDevice, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.device_model

	class Meta:
		verbose_name = "Модель приладу"
		verbose_name_plural = "Моделі приладів"

#this is model repair status
class RepairStatus(models.Model):
	repair_status = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.repair_status

	class Meta:
		verbose_name = "Стан ремонту"
		verbose_name_plural = "Статуси ремонту"

#this is model pay repair status
class PayRepairStatus(models.Model):
	pay_repair_status = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.pay_repair_status

	class Meta:
		verbose_name = "Стан оплати"
		verbose_name_plural = "Статуси оплати"

#this is model for delivery method
class DeliveryMethod(models.Model):
	delivery_method = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.delivery_method

	class Meta:
		verbose_name = "Спосіб доставки"
		verbose_name_plural = "Спосіб доставки"

#this is model for the warranty period
class WarrantyPeriod(models.Model):
	warranty_periods = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.warranty_periods

	class Meta:
		verbose_name = "Терміни гарантії"
		verbose_name_plural = "Термін гарантії"

#this is model for the warranty status 
class WarrantyStatus(models.Model):
	warranty_status = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.warranty_status

	class Meta:
		verbose_name = "Статуси гарантій"
		verbose_name_plural = "Статуси гарантії"

#this is repair model for the client database  
class RepairClient(models.Model):
	name_client = models.CharField(max_length=64, blank=True, null=True, default=None)
	lastname_client = models.CharField(max_length=64, blank=True, null=True, default=None)
	fathername_client = models.CharField(max_length=64, blank=True, null=True, default=None)
	custumer_phone = models.CharField(max_length=24, blank=True, null=True, default=None)
	custumer_email = models.EmailField(max_length=128)
	client_work_place = models.CharField(max_length=400, blank=True, null=True, default=None)
	client_edrpou = models.CharField(max_length=24, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s %s" % (self.lastname_client, self.custumer_phone)

	class Meta:
		verbose_name = "Клієнт з ремонту"
		verbose_name_plural = "Клієнти з ремонту"

#this is model for devices from repair
class RepairDevice(models.Model):
	type_devices = models.ForeignKey(TypeDevice, on_delete=models.CASCADE)
	model_device = models.ForeignKey(ModelDevice, on_delete=models.CASCADE)
	inventory_number = models.CharField(max_length=64, blank=True, null=True, default=None)
	serial_number = models.CharField(max_length=64, blank=True, null=True, default=None)
	repair_status = models.ForeignKey(RepairStatus, on_delete=models.CASCADE)
	pay_status = models.ForeignKey(PayRepairStatus, on_delete=models.CASCADE)
	need_spare_part = models.CharField(max_length=512, blank=True, null=True, default=None)
	method_delivery = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE, default=1)
	invoice = models.CharField(max_length=64, blank=True, null=True, default=None)
	client_malfunction = models.TextField(blank=True, null=True, default=None)
	complete_set_device = models.TextField(blank=True, null=True, default=None)
	select_user = models.ForeignKey(RepairClient, on_delete=models.CASCADE)
	add_comment = models.TextField(blank=True, null=True, default=None)

	mulfunction = models.TextField(blank=True, null=True, default=None)
	price_repair = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	recommendations_repair = models.TextField(blank=True, null=True, default=None)
	recommendations_repair_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	all_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.CASCADE)
	status_warranty = models.ForeignKey(WarrantyStatus, on_delete=models.CASCADE)
	start_warranty = models.DateTimeField(blank=True, null=True, default=None)
	stop_warranty = models.DateTimeField(blank=True, null=True, default=None)

	agreed_work_repair = models.TextField(blank=True, null=True, default=None)
	agreed_work_repair_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	performed_work = models.TextField(blank=True, null=True, default=None)
	materials = models.TextField(blank=True, null=True, default=None)

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s %s" % (self.type_devices, self.model_device)

	class Meta:
		verbose_name = "Прилад з ремонту"
		verbose_name_plural = "Прилади з ремонту"