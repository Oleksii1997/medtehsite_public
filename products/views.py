from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import *
from django.core.paginator import Paginator

def sub_category_products_page(request):
	sub_category = SectionCategoryGoods.objects.filter(is_active=True)
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	return render(request, "section_category_products.html",locals())

def category_products_page(request, sub_category_id):
	category_products = CategoryGoods.objects.filter(section_category__id=sub_category_id, is_active=True)
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	return render(request, "category_products.html",locals())

def products_some_category(request, category_id, page_now_number=1):

	category_products = CategoryGoods.objects.filter(is_active=True)
	brands = BrandProducts.objects.filter(is_active=True).order_by('brand_name')

	some_category = ProductImage.objects.all()
	#for get category products for <h2> tags in html file, this is title
	category_name = CategoryGoods.objects.get(id=category_id)
	category_product_photo = some_category.filter(product__product_category__id=category_id, product__is_active=True, is_main_image=True)
	session_key = request.session.session_key
	curent_page = Paginator(category_product_photo,16)#16 товарів на одній сторінці
	page_list = curent_page.page(page_now_number)
	if not session_key:
		request.session.cycle_key()

	return render(request, "products_some_category.html", locals())

def product_page(request, product_id):
	some_product = ProductImage.objects.all()
	#get queryset the photo selected product
	select_product_photo = some_product.filter(product__id=product_id, is_active=True)
	#get selected product
	select_product = Product.objects.get(id=product_id, is_active=True)
	if select_product.product_discount != 0:
		new_price = select_product.product_price - (select_product.product_price*select_product.product_discount/100)
	
	#sesion key 
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	return render(request, "product_page.html", locals())

def product_filter(request, page_now_number=1):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	category_products = CategoryGoods.objects.filter(is_active=True)
	brands = BrandProducts.objects.filter(is_active=True).order_by('brand_name')
	if request.POST:
		data = request.POST

		has_select_brand = 'list_brand' in data
		has_select_category = 'list_category' in data
		if (has_select_brand and has_select_category):
			select_brand = list(map(int, data.getlist('list_brand')))
			select_category = list(map(int, data.getlist('list_category')))
			products = ProductImage.objects.filter(product__compatible_product_brand__pk__in=select_brand, product__product_category__pk__in=select_category, product__is_active=True, is_main_image=True).distinct()
		elif (has_select_brand and has_select_category==False):
			select_brand = list(map(int, data.getlist('list_brand')))
			select_category = []
			products = ProductImage.objects.filter(product__compatible_product_brand__pk__in=select_brand, product__is_active=True, is_main_image=True).distinct()
		elif (has_select_brand==False and has_select_category):
			select_brand = []
			select_category = list(map(int, data.getlist('list_category')))
			products = ProductImage.objects.filter(product__product_category__pk__in=select_category, product__is_active=True, is_main_image=True).distinct()
		else:
			select_brand = []
			select_category = []
			products = []
		request.session['brand'] = select_brand      #зберігаємо дані в сесію.distinct()
		request.session['category'] = select_category
	else:
		select_brand = request.session['brand']      #беремо дані з сесії
		select_category = request.session['category']
		if (len(select_brand)!=0 and len(select_category)!=0):
			products = ProductImage.objects.filter(product__compatible_product_brand__pk__in=select_brand, product__product_category__pk__in=select_category, product__is_active=True, is_main_image=True).distinct()
		elif (len(select_brand)!=0 and len(select_category)==0):
			products = ProductImage.objects.filter(product__compatible_product_brand__pk__in=select_brand, product__is_active=True, is_main_image=True).distinct()
		elif (len(select_brand)==0 and len(select_category)!=0):
			products = ProductImage.objects.filter(product__product_category__pk__in=select_category, product__is_active=True, is_main_image=True).distinct()
		else:
			select_brand = []
			select_category = []
			products = []#якщо користувач не вибрав ніякі параметри фільтрації, то ніякі товари не повертаємо

	curent_page = Paginator(products,16)#16 товарів на одній сторінці
	page_list = curent_page.page(page_now_number)
	return render(request, "filtration_result.html", locals())