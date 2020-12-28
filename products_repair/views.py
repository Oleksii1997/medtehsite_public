from django.http import HttpResponse
from django.shortcuts import render
from products_repair.models import *
from users.models import *
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from email_sending.views import SendingEmail

def category_repair_page(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	category_repairs = ProductsRepairCategory.objects.filter(is_active=True)
	return render(request,"category_repair.html",locals())

def repair_some_category(request,category_repair_id):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	#Отримуємо інформацію про користувача якщо він авторизований
	have_user = UsersAuthorisation.objects.filter(session_key=session_key ,authorisation_status=True)
	if have_user:
		user_login = UsersAuthorisation.objects.get(session_key=session_key ,authorisation_status=True).username
		User = get_user_model()
		user_information = User.objects.get(username=user_login)
	else:
		print("no user")
	category_name = ProductsRepairCategory.objects.get(id=category_repair_id, is_active=True).product_category_name
	repair_images = RepairedProductsImage.objects.filter(category__product_category_name=category_name, is_active=True)
	repair_descriptions = RepairWorkDescription.objects.filter(category__product_category_name=category_name, is_active=True)
	return render(request,"repair_some_category.html",locals())

def need_consultation(request):
	data=request.POST
	device_dict=dict()
	device_dict["name_client"]=data["name_client"]
	device_dict["phone_client"]=data["phone_client"]
	device_dict["email_client"]=data["email_client"]

	email = SendingEmail()
	email.send_help_repair(device=device_dict)
	print(device_dict)
	return_data=dict()
	return_data["send_status"]=True
	return JsonResponse(return_data, safe=False)

