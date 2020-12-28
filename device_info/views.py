from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import AddDeviceForm
from django.http import JsonResponse
from django.db.models import Q
from email_sending.views import SendingEmail
from datetime import datetime, date
from datetime import timedelta



#function for add new device in the repair database 
def new_device(request):
	devices = TypeDevice.objects.filter(is_active=True).order_by("device_type")
	model_devices = ModelDevice.objects.filter(is_active=True).order_by("type_device")
	status_repair = RepairStatus.objects.filter(is_active=True)
	method_delivery = DeliveryMethod.objects.filter(is_active=True)
	register_users = RepairClient.objects.filter(is_active=True).order_by("lastname_client")
	warrantys = WarrantyPeriod.objects.filter(is_active=True)
	pay_status = PayRepairStatus.objects.filter(is_active=True)
	form = AddDeviceForm(request.POST or None)

	if request.POST:
		get_device = request.POST
		length_email = len(get_device["custumer_email"])#to determine whether to save a registered user or created by us (if length 0 - save from the database)
		if len(get_device["price_repair"])!=0:
			price = round((float(get_device["price_repair"])+float(get_device["recommendations_repair_price"])),2)
		else:
			price = 0
		#this is for sending email
		if get_device["send_email"]=="True" or get_device["pay_send_email"]=="True":
			device_dict=get_device.copy()#!!!!!!!!!!
			if len(get_device["custumer_email"])==0:
				client=RepairClient.objects.get(id=get_device["select_user"])
				device_dict["name_client"]=client.name_client
				device_dict["fathername_client"]=client.fathername_client
				device_dict["lastname_client"]=client.lastname_client
				device_dict["custumer_phone"]=client.custumer_phone
				device_dict["custumer_email"]=client.custumer_email
				device_dict["client_work_place"]=client.client_work_place
				device_dict["client_edrpou"]=client.client_edrpou
			
			device_dict["type_devices"]=TypeDevice.objects.get(id=get_device["type_devices"]).device_type
			device_dict["model_device"]=ModelDevice.objects.get(id=get_device["model_device"]).device_model
			device_dict["repair_status_value"]=RepairStatus.objects.get(id=device_dict["repair_status"]).repair_status
			device_dict["method_delivery_value"]=DeliveryMethod.objects.get(id=device_dict["method_delivery"]).delivery_method
			device_dict["warranty_period_value"]=WarrantyPeriod.objects.get(id=device_dict["warranty_period"]).warranty_periods
			device_dict["pay_repair_status_value"]=PayRepairStatus.objects.get(id=device_dict["pay_repair_status"]).pay_repair_status
			device_dict["all_price"]=price
			
			if get_device["send_email"]=="True":
				email = SendingEmail()
				email.send_new_device(device=device_dict)
			if get_device["pay_send_email"]=="True":
				email = SendingEmail()
				email.send_pay_repair(device=device_dict)
		else:
			print("False")
		if length_email>0:
			create_new_user = RepairClient.objects.create(name_client=get_device["name_client"].lower(), lastname_client=get_device["lastname_client"].lower(),
															fathername_client=get_device["fathername_client"].lower(), custumer_phone=get_device["custumer_phone"],
															custumer_email=get_device["custumer_email"], client_work_place=get_device["client_work_place"].lower(),
															client_edrpou=get_device["client_edrpou"], is_active=True)

			device = TypeDevice.objects.get(id=get_device["type_devices"])
			device_models = ModelDevice.objects.get(id=get_device["model_device"])
			repair_device_status = RepairStatus.objects.get(id=get_device["repair_status"])
			warranty_status = WarrantyStatus.objects.get(id=1)#При додаванні нового приладу статус гарантії "Гарантія ще не розпочата" (id=1), змінити цей статус можна в updated device
			
			delivery = DeliveryMethod.objects.get(id=get_device["method_delivery"])
			warranty = WarrantyPeriod.objects.get(id=get_device["warranty_period"])
			pay_device_status = PayRepairStatus.objects.get(id=get_device["pay_repair_status"])

			new_device = RepairDevice.objects.create(type_devices=device, model_device=device_models, inventory_number=(get_device["inventory_number"]).lower(),
														serial_number=(get_device["serial_number"]).lower(), repair_status=repair_device_status, pay_status=pay_device_status,
														need_spare_part=get_device["need_spare_part"], method_delivery=delivery, invoice=get_device["invoice"],
														client_malfunction=get_device["client_malfunction"], complete_set_device=get_device["complete_set_device"], select_user=create_new_user, 
														add_comment=get_device["add_comment"], mulfunction=get_device["mulfunction"], price_repair=get_device["price_repair"],
														recommendations_repair=get_device["recommendations_repair"], recommendations_repair_price=get_device["recommendations_repair_price"],
														all_price=price, warranty_period=warranty, status_warranty=warranty_status, agreed_work_repair=get_device["agreed_work_repair"], agreed_work_repair_price=get_device["agreed_work_repair_price"],
														performed_work=get_device["performed_work"], materials=get_device["materials"], is_active=True)#save device in model.RepairDevice
		
			return redirect('/device/add_device_user_maked')
		
		else:
			device = TypeDevice.objects.get(id=get_device["type_devices"])
			device_models = ModelDevice.objects.get(id=get_device["model_device"])
			repair_device_status = RepairStatus.objects.get(id=get_device["repair_status"])
			client = RepairClient.objects.get(id=get_device["select_user"])
			delivery = DeliveryMethod.objects.get(id=get_device["method_delivery"])
			warranty = WarrantyPeriod.objects.get(id=get_device["warranty_period"])
			warranty_status = WarrantyStatus.objects.get(id=1)
			pay_device_status = PayRepairStatus.objects.get(id=get_device["pay_repair_status"])

			new_device = RepairDevice.objects.create(type_devices=device, model_device=device_models, inventory_number=(get_device["inventory_number"]).lower(),
														serial_number=(get_device["serial_number"]).lower(), repair_status=repair_device_status, pay_status=pay_device_status, need_spare_part=get_device["need_spare_part"],
														method_delivery=delivery, invoice=get_device["invoice"], client_malfunction=get_device["client_malfunction"],
														complete_set_device=get_device["complete_set_device"], select_user=client, add_comment=get_device["add_comment"], mulfunction=get_device["mulfunction"],
														price_repair=get_device["price_repair"], recommendations_repair=get_device["recommendations_repair"],
														recommendations_repair_price=get_device["recommendations_repair_price"], all_price=price, warranty_period=warranty, status_warranty=warranty_status,
														agreed_work_repair=get_device["agreed_work_repair"], agreed_work_repair_price=get_device["agreed_work_repair_price"], performed_work=get_device["performed_work"],
														materials=get_device["materials"], is_active=True)#save device in model.RepairDevice
			return redirect('/device/add_device_maked')
	return render(request, "add_new_device.html", locals())

#successed the creating new device	and user
def maked_device_user(request):
	return render(request, "device_user_maked.html")

#successed the creating new device
def maked_device(request):
	return render(request, "device_maked.html")

#this is for all device in panel administrator
def all_device_database(request):
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

	devices = RepairDevice.objects.filter(is_active=True, created__range=(from_date,to_date_search)).values("id","type_devices__device_type","model_device__device_model",
																	"select_user__name_client", "select_user__lastname_client",
																	"select_user__fathername_client", "select_user__custumer_phone", "select_user__client_work_place", 
																	"select_user__client_edrpou", "repair_status__repair_status", "pay_status__pay_repair_status", "created", "updated")
	return render(request, "device_datatable.html", locals())

#this is for all user in panel administrator
def all_client(request):
	clients = RepairClient.objects.filter(is_active=True).values("id","name_client","lastname_client","fathername_client",
																	"custumer_phone", "custumer_email", "client_work_place", "client_edrpou","created")
	return render(request, "client_datatable.html", locals())

#this is for update device information
def updated_device_info(request, device_id):
	devices = TypeDevice.objects.filter(is_active=True).order_by("device_type")
	status_repair = RepairStatus.objects.filter(is_active=True)
	model_devices = ModelDevice.objects.filter(is_active=True).order_by("type_device")
	method_delivery=DeliveryMethod.objects.filter(is_active=True)
	warrantys = WarrantyPeriod.objects.filter(is_active=True)
	pay_status = PayRepairStatus.objects.filter(is_active=True)

	device_info = RepairDevice.objects.get(id=device_id)
	form = AddDeviceForm(request.POST or None)
	if request.POST:
		data = request.POST
		device_type_new = TypeDevice.objects.get(id=data["type_devices"])
		device_model_new = ModelDevice.objects.get(id=data["model_device"])
		repair_status_new = RepairStatus.objects.get(id=data["repair_status"])
		price = round((float(data["price_repair"])+float(data["recommendations_repair_price"])),2)
		warranty = WarrantyPeriod.objects.get(id=data["warranty_period"])
		pay_device_status = PayRepairStatus.objects.get(id=data["pay_repair_status"])
		date_updated = datetime.now()
		
		RepairDevice.objects.filter(id=device_id).update(type_devices=device_type_new, model_device=device_model_new,
														inventory_number=data["inventory_number"], serial_number=data["serial_number"],
														client_malfunction=data["client_malfunction"],repair_status=repair_status_new, pay_status=pay_device_status,
														need_spare_part=data["need_spare_part"], method_delivery=data["method_delivery"],
														invoice=data["invoice"], complete_set_device=data["complete_set_device"], add_comment=data["add_comment"],
														mulfunction=data["mulfunction"], price_repair=data["price_repair"],
														recommendations_repair=data["recommendations_repair"], recommendations_repair_price=data["recommendations_repair_price"],
														all_price=price, warranty_period=warranty, agreed_work_repair=data["agreed_work_repair"],
														agreed_work_repair_price=data["agreed_work_repair_price"], performed_work=data["performed_work"], materials=data["materials"],
														updated=date_updated)
		#Якщо обрали "Розпочати гарантійний період?" (Так), то записуємо дату початку та кінця гарантії
		if data["start_warranty_period"]=="True":
			warranty_status = WarrantyStatus.objects.get(id=2)#Гарантійний статус - "Гарантійний термін триває"
			start_warranty_date = datetime.now()
			if int(data["warranty_period"])==1:
				stop_warranty_date = start_warranty_date + timedelta(days=90)
			elif int(data["warranty_period"])==2:
				stop_warranty_date = start_warranty_date + timedelta(days=180)
			else:
				stop_warranty_date = start_warranty_date + timedelta(days=364)
			RepairDevice.objects.filter(id=device_id).update(status_warranty=warranty_status, start_warranty=start_warranty_date, stop_warranty=stop_warranty_date)
		#this is for sending email
		if data["send_email"]=="True" or data["pay_send_email"]=="True":
			device_dict=data.copy()
		
			device_dict["name_client"]=device_info.select_user.name_client
			device_dict["fathername_client"]=device_info.select_user.fathername_client
			device_dict["lastname_client"]=device_info.select_user.lastname_client
			device_dict["custumer_phone"]=device_info.select_user.custumer_phone
			device_dict["custumer_email"]=device_info.select_user.custumer_email
			device_dict["client_work_place"]=device_info.select_user.client_work_place
			device_dict["client_edrpou"]=device_info.select_user.client_edrpou
	
			device_dict["type_devices"]=TypeDevice.objects.get(id=device_dict["type_devices"]).device_type
			device_dict["model_device"]=ModelDevice.objects.get(id=device_dict["model_device"]).device_model
			device_dict["repair_status_value"]=RepairStatus.objects.get(id=device_dict["repair_status"]).repair_status
			device_dict["method_delivery_value"]=DeliveryMethod.objects.get(id=device_dict["method_delivery"]).delivery_method
			device_dict["warranty_period_value"]=WarrantyPeriod.objects.get(id=device_dict["warranty_period"]).warranty_periods
			device_dict["pay_repair_status_value"]=PayRepairStatus.objects.get(id=device_dict["pay_repair_status"]).pay_repair_status
			device_dict["all_price"]=price
			
			if data["send_email"]=="True":
				email = SendingEmail()
				email.send_new_device(device=device_dict)
			if data["pay_send_email"]=="True":
				email = SendingEmail()
				email.send_pay_repair(device=device_dict)
		else:
			print("False")

		return redirect('/device/all_devices')
	return render(request, "update_device.html", locals())

#this is for all active device in panel administrator (devices in the repair)
def all_device_database_active(request):
	devices = RepairDevice.objects.filter(is_active=True, repair_status__pk__in=[1,2,3,4,5]).values("id","type_devices__device_type","model_device__device_model",
																	"select_user__name_client", "select_user__lastname_client",
																	"select_user__fathername_client", "select_user__custumer_phone", "select_user__client_work_place", 
																	"select_user__client_edrpou", "repair_status__repair_status", "updated")
	return render(request, "active_device_datatable.html", locals())
	
#for add new device type or model in the repair database
def add_type_model(request):
	if request.POST:
		data=request.POST
		all_type_device = TypeDevice.objects.filter(is_active=True).values_list('device_type', flat=True)
		all_type = [x.lower() for x in all_type_device]
		now_type = data["device_type"].lower()
		if now_type in all_type:
			type_set = TypeDevice.objects.filter(is_active=True).values('id', 'device_type')
			for device in type_set:
				if device["device_type"].lower() ==now_type:
					device_type = TypeDevice.objects.get(id=device["id"])
					ModelDevice.objects.create(device_model=data["device_model"], type_device=device_type, is_active=True)
		else:
			device_type = TypeDevice.objects.create(device_type=data["device_type"], is_active=True)
			ModelDevice.objects.create(device_model=data["device_model"], type_device=device_type, is_active=True)
		return redirect('/device/add_device')
	else:
		return render(request, "add_type_model.html", locals())

#this is for search type device or model 
def search_type_device(request):
	data=request.POST
	model_select_device = ModelDevice.objects.filter(type_device__id=data["search_type_device"],is_active=True)
	return_date=[]
	for device in model_select_device:
		return_dict=dict()
		return_dict["id"]=device.id
		return_dict["device_model"]=device.device_model
		return_date.append(return_dict)
	return JsonResponse(return_date, safe=False)
 
def search_model_device(request):
	data=request.POST
	type_select_device = ModelDevice.objects.get(id=data["search_model_device"]).type_device.id
	return_date=type_select_device
	return JsonResponse(return_date, safe=False)

#this is for search user (ajax)
def search_user(request):
	return_list_search=[]
	data = request.POST
	if request.POST:
		search_request = data["search_request"]
		filter_client = RepairClient.objects.filter(Q(custumer_phone__icontains=search_request)|Q(custumer_email__icontains=search_request)|
													Q(client_work_place__icontains=search_request.lower())|Q(name_client__icontains=search_request.lower())|
													Q(lastname_client__icontains=search_request.lower())|Q(fathername_client__icontains=search_request.lower())|
													Q(client_edrpou__icontains=search_request))

		for client in filter_client:
			user_dict=dict()
			user_dict["id"]=client.id
			user_dict["custumer_phone"]=client.custumer_phone
			user_dict["name_client"]=client.name_client.title()
			user_dict["fathername_client"]=client.fathername_client.title()
			user_dict["lastname_client"]=client.lastname_client.title()
			return_list_search.append(user_dict)

	return JsonResponse(return_list_search, safe=False)

def unpaid_repair_device(request):
	unpaid_devices=RepairDevice.objects.filter(pay_status__pk__in=[2,3]).values("id", "type_devices__device_type", "model_device__device_model",
																					"select_user__name_client", "select_user__fathername_client",
																					"select_user__lastname_client", "select_user__custumer_phone","select_user__client_work_place", 
																					"select_user__client_edrpou", "repair_status__repair_status", "pay_status__pay_repair_status", "created","updated")
	return render(request, "unpaid_repair_device.html", locals())

# view_user_devices and inform_repair for page "Повідомити про стан ремонту"
def view_user_devices(request):
	user_device_list = []
	if request.POST:
		data = request.POST
		
		if data["calendar_from"]:
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

		devices = RepairDevice.objects.filter(select_user__id=data["select_user_id"], updated__range=(from_date,to_date_search)).order_by('-updated')
		for device in devices:
			device_dict = dict()
			device_dict["id"]=device.id
			device_dict["type_devices"]=device.type_devices.device_type
			device_dict["model_device"]=device.model_device.device_model
			device_dict["repair_status"]=device.repair_status.repair_status
			device_dict["pay_status"]=device.pay_status.pay_repair_status
			device_dict["created"]=device.created.strftime("%d-%m-%Y")
			device_dict["updated"]=device.updated.strftime("%d-%m-%Y")
			user_device_list.append(device_dict)

	return JsonResponse(user_device_list, safe=False)

def inform_repair(request):
	#Для загрузки початкових даних на сторінку inform_repair.html
	to_date = datetime.now()
	from_date = to_date - timedelta(days=30)
	max_date = datetime.now()	
	register_users =RepairClient.objects.filter(is_active=True).order_by("lastname_client")
	number_users = register_users.count()
	form = AddDeviceForm(request.POST or None)
	
	#Обробка отриманих даних з форми (action="{% url 'inform_repair' %}") , відправка e-mail
	if request.POST:
		data = request.POST
		#створюємо словар який містить "Добатковий коментар" та обрані прилади з форми на сторінці inform_repair.html
		email_data_dict = dict()
		email_data_dict["add_comment"]=data["add_comment"]

		user_selected = RepairClient.objects.get(id=data["select_user"])
		email_data_dict["select_user_email"]=user_selected.custumer_email
		selected_devices = list(map(int, request.POST.getlist('selected_device')))
		
		device_selected = RepairDevice.objects.filter(pk__in=selected_devices)
		select_device_list = list()
		for device in device_selected:
			device_dict = dict()
			device_dict["id"]=device.id
			device_dict["type_devices"]=device.type_devices.device_type
			device_dict["model_device"]=device.model_device.device_model
			device_dict["inventory_number"]=device.inventory_number
			device_dict["serial_number"]=device.serial_number
			device_dict["repair_status"]=device.repair_status.repair_status
			device_dict["repair_status_id"]=device.repair_status.id
			device_dict["pay_status"]=device.pay_status.pay_repair_status
			device_dict["method_delivery"]=device.method_delivery.delivery_method
			device_dict["invoice"]=device.invoice
			device_dict["client_malfunction"]=device.client_malfunction
			device_dict["complete_set_device"]=device.complete_set_device
			device_dict["mulfunction"]=device.mulfunction
			device_dict["price_repair"]=device.price_repair
			device_dict["recommendations_repair"]=device.recommendations_repair
			device_dict["recommendations_repair_price"]=device.recommendations_repair_price
			device_dict["all_price"]=device.all_price
			device_dict["warranty_period"]=device.warranty_period.warranty_periods
			device_dict["agreed_work_repair"]=device.agreed_work_repair
			device_dict["agreed_work_repair_price"]=device.agreed_work_repair_price
			device_dict["performed_work"]=device.performed_work
			select_device_list.append(device_dict)

		email_data_dict["selected_device"] = select_device_list

		email = SendingEmail()
		email.send_inform_repair(device=email_data_dict)
		return render(request, "inform_repair_email_success.html", locals())
		
	return render(request, "inform_repair.html", locals())

def advertising_mail(request):
	all_client=RepairClient.objects.filter(is_active=True)
	if request.POST:
		data=request.POST;
		print(data)

		email_info_dict=dict()
		email_info_dict["text_email"]=data["text_email"]

		selected_client = list(map(int, data.getlist('list_email_checkbox')))
		clients=RepairClient.objects.filter(is_active=True, pk__in=selected_client)
		email_list=[]
		for client in clients:
			email_list.append(client.custumer_email)
		email_add_address = list(map(str, data.getlist('list_add_email')))
		email_list=email_list+email_add_address
		email_info_dict["email"]=email_list
		length_email_list=len(email_list)
		print(email_info_dict)
		if len(email_list)==0:
			print("no")
		else:
			email = SendingEmail()
			email.send_advertising_mail(device=email_info_dict)
			
		return render(request, "advertis_email_success.html", locals())

	return render(request, "advertising_mail.html", locals())