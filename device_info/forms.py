from django import forms
from .models import *

class AddDeviceForm(forms.Form):
	type_devices = forms.CharField(required=True)
	model_device = forms.CharField(required=True)
	inventory_number = forms.CharField(required=True)
	serial_number = forms.CharField(required=True)
	client_malfunction = forms.CharField(widget=forms.Textarea, required=True)
	repair_status = forms.CharField(required=True)
	status_warranty = forms.CharField(required=True)
	pay_repair_status = forms.CharField(required=True)
	need_spare_part = forms.CharField(required=False)
	method_delivery= forms.CharField(required=False)
	invoice = forms.CharField(required=False)
	complete_set_device = forms.CharField(widget=forms.Textarea, required=True) 
	add_comment = forms.CharField(widget=forms.Textarea, required=False)

	select_user = forms.CharField(required=False)

	name_client = forms.CharField(required=False)
	lastname_client = forms.CharField(required=False)
	fathername_client = forms.CharField(required=False)
	custumer_phone = forms.CharField(required=False)
	custumer_email = forms.EmailField(required=False)
	client_work_place = forms.CharField(required=False)
	client_edrpou = forms.CharField(required=False)
	
	mulfunction = forms.CharField(widget=forms.Textarea, required=False)
	price_repair = forms.DecimalField(required=False)
	recommendations_repair = forms.CharField(widget=forms.Textarea, required=False)
	recommendations_repair_price = forms.DecimalField(required=False)
	warranty_period = forms.CharField(required=False)

	agreed_work_repair = forms.CharField(widget=forms.Textarea, required=False)
	agreed_work_repair_price = forms.DecimalField(required=False)

	performed_work = forms.CharField(widget=forms.Textarea, required=False)
	materials = forms.CharField(widget=forms.Textarea, required=False)

