from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UsersAuthorisation
from .context_processors import getting_authenticate_info
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.template.context_processors import csrf

from django import forms
from email_sending.views import SendingEmail

from django.contrib.auth.models import User
import random

def login(request):
	if request.POST:
		login_dict = dict()
		data = request.POST
		username = data.get("username")
		password = data.get("password")
		login_dict["username"] = username
		login_dict["password"] = password
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			login_dict["login_success"] = True
			getting_authenticate_info(request)
			session_key = request.session.session_key
			if not session_key:
				request.session.cycle_key()
			authenticate_user, authenticate_user_new = UsersAuthorisation.objects.get_or_create(username=username, authorisation_status=True, session_key=session_key)
			login_dict["need_authorisarion_text"] = True
		else:
			login_dict["login_success"] = False
			login_dict["need_authorisarion_text"] = False

		return JsonResponse(login_dict)

def logout(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	UsersAuthorisation.objects.filter(session_key=session_key).update(authorisation_status=False)
	auth.logout(request)
	return redirect('/')

def registration_new_user(request):
	args = {}
	args.update(csrf(request))
	args['form'] = SignUpForm()
	if request.POST:
		newuser_form = SignUpForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])#avtomatical login the created user
			auth.login(request,newuser)
			
			session_key = request.session.session_key
			if not session_key:
				request.session.cycle_key()
			authenticate_user, authenticate_user_new = UsersAuthorisation.objects.get_or_create(username=newuser_form.cleaned_data['username'], authorisation_status=True, session_key=session_key)#avtomatical view login the created user
			
			email = SendingEmail()
			email.successfully_registration_email(login_new_user=newuser_form.cleaned_data['username'], email_new_user=newuser_form.cleaned_data['email'])
			return redirect('/')
		else:
			args['form'] = newuser_form
	return render(request, "registration_new_user.html", args)

def recovery_password(request):
	if request.POST:
		print("recovery password")
		print(request.POST)
		user_recovery = User.objects.filter(username=request.POST['username'])
		recovery_dict=dict()
		if user_recovery:
			print("yes")
			for user_info in user_recovery:
				recovery_dict["email"]=user_info.email
			recovery_dict["user"]=True

			#generate password
			chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
			password = ''
			for x in range(16):
				password += random.choice(chars)

			user = User.objects.get(username=request.POST['username'])
			user.set_password(password)
			user.save()

			password_info = dict()
			password_info["password"]=password
			password_info["email"]=recovery_dict["email"]
			email = SendingEmail()
			email.email_recovery_password(new_password_info=password_info)

		else:
			recovery_dict["email"]=None
			recovery_dict["user"]=False
	return JsonResponse(recovery_dict)

def change_password_form(request):
	return render(request, "change_password.html")

def change_password(request):
	if request.POST:
		data = request.POST
		reply_ajax = dict()
		reply_ajax["username_valid"]=False
		reply_ajax["old_password_valid"]=False
		reply_ajax["same_password"]=False
		reply_ajax["password_change"]=False
		#Перевіряємо чи існує такий користувач та чи правильний пароль
		user_recovery = User.objects.filter(username=data['username'])
		if user_recovery:
			reply_ajax["username_valid"]=True
			for select_user in user_recovery:
				user = auth.authenticate(username=data['username'], password=data['old_password'])
				if user is not None:
					reply_ajax["old_password_valid"]=True
					if data["new_password"]==data["repeat_new_password"]:#чи однаковий новий пароль і його підтвердження
						reply_ajax["same_password"]=True
						if data["valid_password_1"] == 'true': #чи відповідає пароль критеріям складності (перевірка в js)
							
							user = User.objects.get(username=data['username'])#змінюємо пароль в базі даних
							user.set_password(data["new_password"])
							user.save()

							password_info = dict()#відправляємо лист про зміну пароля
							password_info["email"]=user.email
							email = SendingEmail()
							email.email_change_password(new_password_info=password_info)

							reply_ajax["password_change"]=True
						else:
							reply_ajax["password_change"]=False
					else:
						reply_ajax["same_password"]=False
				else:
					reply_ajax["old_password_valid"]=False
		else:
			reply_ajax["username_valid"]=False

	return JsonResponse(reply_ajax)
