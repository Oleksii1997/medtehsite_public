from django.http import HttpResponse
from django.shortcuts import render, redirect
from orders.models import *
from users.models import *
from device_info.models import *
from datetime import datetime, date
from datetime import timedelta

#for the PDF generation
from django import template
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
import os
from django.conf import settings



#для правильного відображення товарів замовника, щоб в одному замовленні було декілька товарів
def sortedje_orders(request, filter_orders):
	orders = filter_orders
	all_user_orders = list()
	for order_filtr in orders:
		item_order = dict()
		item_order["order_id"]=order_filtr.order.id
		item_order["total_price_order"]=order_filtr.order.total_price
		item_order["status"]=order_filtr.order.status
		item_order["created"]=order_filtr.order.created
		
		products = list()
		item_product = dict()
		item_product["product_name"]=order_filtr.product.product_name
		item_product["number"]=order_filtr.number
		item_product["product_price"]=order_filtr.product_price
		item_product["total_price_item"]=order_filtr.total_price
		products.append(item_product)
		item_order["products"]=products

		if len(all_user_orders)==0:
			all_user_orders.append(item_order)
		else:
			all_id_order = list()
			for all_user_order in all_user_orders:
				id_order = all_user_order["order_id"]
				id_now = item_order["order_id"]
				if id_order==id_now:
					all_user_order["products"].append(item_product)
				all_id_order.append(id_order)
			if id_now not in all_id_order:
				all_user_orders.append(item_order)
	return all_user_orders

#function for view orders for the last time period (default - 1 month)
def view_orders(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	if request.POST:
		data = request.POST
		from_date =data["calendar_from"].split("-")#returned the date in  format ['Y','m','d']
		to_date =data["calendar_to"].split("-")		
	else:
		to_date = datetime.now()
		from_date = to_date - timedelta(days=30)
		to_date = [to_date.year, to_date.month, to_date.day]
		from_date = [from_date.year, from_date.month, from_date.day]

	max_date = datetime.now()
	to_date = date(int(to_date[0]), int(to_date[1]), int(to_date[2]))
	from_date = date(int(from_date[0]), int(from_date[1]), int(from_date[2]))

	if to_date<from_date:
		from_date, to_date=to_date, from_date
	to_date_search = to_date + timedelta(days=1)#becous __range do not include last day
	
	username = UsersAuthorisation.objects.get(session_key=session_key ,authorisation_status=True).username#get username (it is phone number ) for the orders filter
	filter_orders = ProductInOrder.objects.filter(order__custumer_phone=username, created__range=(from_date,to_date_search))

	all_user_orders=sortedje_orders(request, filter_orders=filter_orders)

	all_user_order = len(all_user_orders)
	return render(request, "office_user_orders.html", locals())

# function for visualisation the  client  repairs in the user office
def view_repair(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	if request.POST:
		data = request.POST
		from_date =data["calendar_from"].split("-")#returned the date in  format ['Y','m','d']
		to_date =data["calendar_to"].split("-")		
	else:
		to_date = datetime.now()
		from_date = to_date - timedelta(days=30)
		to_date = [to_date.year, to_date.month, to_date.day]
		from_date = [from_date.year, from_date.month, from_date.day]

	max_date = datetime.now()
	to_date = date(int(to_date[0]), int(to_date[1]), int(to_date[2]))
	from_date = date(int(from_date[0]), int(from_date[1]), int(from_date[2]))

	if to_date<from_date:
		from_date, to_date=to_date, from_date
	to_date_search = to_date + timedelta(days=1)#becous __range do not include last day

	#now we must get username (it is a phone number client) and filter repair this client
	username = UsersAuthorisation.objects.get(session_key=session_key ,authorisation_status=True).username
	device_repair = RepairDevice.objects.filter(select_user__custumer_phone=username, updated__range=(from_date,to_date_search))
	all_user_repair = len(device_repair)

	return render(request, "office_user_repair.html", locals())

#Функція для відображення детальної інформації про ремонт приладу в особистому кабінеті клієнта
def user_device_repair_info(request, repair_id):
	device = RepairDevice.objects.get(id=repair_id, is_active=True)

	return render(request, "user_device_repair_info.html", locals())

#Функція для генерації pdf таблиці з поточним станом ремонту

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path

def datatable_Repair_PDF(request, repair_id):
	print(repair_id)
	device = RepairDevice.objects.get(id=repair_id, is_active=True)
	print(device)
	data=dict()

	data["device"]=device
	template=get_template("pdf_datatable_repair.html")
	data_p=template.render(data)
	response=BytesIO()
	pdfPage=pisa.CreatePDF(BytesIO(data_p.encode("utf-8")), response, encoding='UTF-8', link_callback=fetch_resources)
	if not pdfPage.err:
		return HttpResponse(response.getvalue(), content_type="application/pdf")

	else:
		return HttpResponse("Error generation PDF")



