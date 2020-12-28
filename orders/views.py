from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from users.models import *
from products.models import ProductImage
from .forms import CheckoutForm
from django.contrib import auth

from django.contrib.auth import get_user_model

from email_sending.views import SendingEmail

def basket_adding(request):
	return_dict = dict()
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	print(request.POST)
	data = request.POST
	product_id = data.get("product_id")
	number = data.get("number")
	is_delete = data.get("is_delete")
	add_item = data.get("add_item")
	minus_item = data.get("minus_item")
	
	if add_item=='true':
		number = int(number)+1
		price_one_item = ProductInBusket.objects.get(id=product_id).product_price
		total_price = price_one_item*number
		ProductInBusket.objects.filter(id=product_id).update(number=number,total_price=total_price)
	elif minus_item=='true':
		number = int(number)-1
		price_one_item = ProductInBusket.objects.get(id=product_id).product_price
		total_price = price_one_item*number
		ProductInBusket.objects.filter(id=product_id).update(number=number,total_price=total_price)
		if number==0:                                                              #if 0 item in busket - the delete products in basket and database
			ProductInBusket.objects.filter(id=product_id).update(is_active=False)
	else:
		if is_delete== 'true':#delete products in busket and database
			ProductInBusket.objects.filter(id=product_id).update(is_active=False)
		else:	
			new_product, created = ProductInBusket.objects.get_or_create(session_key=session_key, is_active=True, product_id=product_id, defaults={"number":number})
			if not created:
				new_product.number += int(number)
				new_product.save(force_update=True)
	#common cod for 2 cases
	products_in_busket = ProductInBusket.objects.filter(session_key=session_key, is_active=True)
	product_total_number = products_in_busket.count()

	return_dict["product_total_number"] = product_total_number
	all_total_price = 0                                   # calculate all total price in orders
	for product_in_buscet in products_in_busket:
		all_total_price += product_in_buscet.total_price
	return_dict["all_total_price"] = all_total_price

	return_dict["products"] = list()

	for item in products_in_busket:
		product_dict = dict()
		product_dict["id"] = item.id#basket id
		product_dict["product_id"] = item.product.id#product id
		product_dict["product_name"] = item.product.product_name
		product_dict["number"] = item.number
		product_dict["product_price"] = item.product_price
		product_dict["total_price"] = item.total_price
		return_dict["products"].append(product_dict)


	return JsonResponse(return_dict)

def checkout(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	products_in_busket = ProductInBusket.objects.filter(session_key=session_key, is_active=True)
	user_login = UsersAuthorisation.objects.get(session_key=session_key ,authorisation_status=True).username
	User = get_user_model()
	user_information = User.objects.get(username=user_login)
	form = CheckoutForm(request.POST or None)
	if request.POST:
		data_orders = request.POST
		total_price = 0
		for product_in_buscet in products_in_busket:
			total_price += product_in_buscet.total_price
		
		if form.is_valid():
			print('yes')
			status_new_order = Status.objects.get(id = "1")
			new_order = Order.objects.create(total_price=total_price,custumer_name=data_orders["custumer_name"],custumer_fathername=data_orders["custumer_fathername"],custumer_surname=data_orders["custumer_surname"],
				custumer_email=data_orders["custumer_email"],custumer_phone=data_orders["custumer_phone"],how_shipping=data_orders["how_shipping"], shipping_address=data_orders["shipping_address"],
				coment_to_order=data_orders["coment_to_order"], status=status_new_order)#save order in model.Order
			for product_in_buscet in products_in_busket:
				ProductInOrder.objects.create(order=new_order,product=product_in_buscet.product,is_active=True,
					number=product_in_buscet.number,product_price=product_in_buscet.product_price,total_price=product_in_buscet.total_price)#save data in models.ProductInOrder

			#sending email
			email = SendingEmail()
			email.sending_email(type_id=1, email=data_orders["custumer_email"], order=products_in_busket, total_price=total_price)#custumer notification
			email.sending_email(type_id=2, custumer=new_order, order=products_in_busket, total_price=total_price)#admin notification
			products_in_busket.update(is_active=False)#for cleened busket
			return redirect('/orders/checkout_maked')
		else:
			print('no')
			print(form.errors)
	return render(request, "checkout.html", locals())

def checkout_maked(request):
	return render(request, "checkout_maked.html")