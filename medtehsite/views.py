from django.http import HttpResponse
from django.shortcuts import render
from products.models import *
from products_repair.models import *
from users.models import *
from django.contrib import auth
from django.contrib.auth import get_user_model


def homepage(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	category_products = CategoryGoods.objects.filter(is_active=True)
	category_repairs = ProductsRepairCategory.objects.filter(is_active=True)
	brands = BrandProducts.objects.filter(is_active=True).order_by('brand_name')
	return render(request, "homepage.html", locals())

def about_us(request):
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
	return render(request, "about_us.html", locals())

def how_we_work(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	return render(request, "how_we_work.html", locals())