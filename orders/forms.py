from django import forms
forms.fields.Field.default_error_messages = {'required':("Поле обов'язкове для заповнення"),'invalid':("Введіть коректну електронну адресу"),}
from .models import *

class CheckoutForm(forms.Form):
	custumer_name = forms.CharField(required=True)
	custumer_fathername = forms.CharField(required=True)
	custumer_surname = forms.CharField(required=True)
	custumer_email = forms.EmailField(required=True)
	custumer_phone = forms.CharField(required=True)
	how_shipping = forms.CharField(required=False)
	shipping_address = forms.CharField(required=False)
	coment_to_order = forms.CharField(widget=forms.Textarea, required=False)