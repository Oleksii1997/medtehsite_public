from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import *

from medtehsite.settings import FROM_EMAIL, EMAIL_ADMIN
from .models import EmailSending

class SendingEmail(object):
	from_email = "Медичне обладнання<%s>" % FROM_EMAIL
	reply_to_emails = [from_email]#email address to reply
	target_emails = []
	bcc_emails = []

	def sending_email(self, type_id, email=None, custumer=None, order=None, total_price=None):
		#if not email, so far it is type id==2 vhich is admin notification
		if not email:
			email = EMAIL_ADMIN

		target_emails = [email]

		vars = {

		}
		if type_id ==1:#custumer notification
			subject = "Ваше замовлення отримане магазином Unimed.kiev.ua"
			vars['order'] = order
			vars['total_price'] = total_price
			message = get_template('email_templates/email_to_custumer.html').render(vars)

		elif type_id == 2:#admin notification
			subject = "Нове замовлення"
			vars['order'] = order
			vars['total_price'] = total_price
			vars['custumer'] = custumer
			message = get_template('email_templates/email_to_admin.html').render(vars)

		email_send_to = EmailType.objects.get(id=type_id)#save in database the sending email
		sendemail_database = EmailSending.objects.create(email_to=email, email_type=email_send_to)
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()

	def successfully_registration_email(self, login_new_user, email_new_user):
		subject = "Реєстрація на сайті unimed.kiev.ua"
		target_emails = [email_new_user]

		vars = {

		}
		vars["login_new_user"]=login_new_user
		message = get_template('email_templates/email_success_registration.html').render(vars)
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()
		print("Email was sent successfully!")

	def send_new_device(self, device):
		target_emails = [device["custumer_email"]]

		vars = device
		#if repair status "Прийнято в ремонт"
		if int(device["repair_status"])==1:#if repair status "Прийнято в ремонт"
			subject = "Надходження приладу в ремонт"
			message = get_template('email_templates/email_get_device_repair.html').render(vars)
		elif int(device["repair_status"])==2:
			subject = "Результати технічного огляду"
			message = get_template('email_templates/email_inspection_repair.html').render(vars)
		elif int(device["repair_status"])==3:
			subject = "Підтвердження початку ремонту"
			message = get_template('email_templates/email_start_repair.html').render(vars)
		elif int(device["repair_status"])==4:
			subject = "Затримка ремонту"
			message = get_template('email_templates/email_wait_spare_repair.html').render(vars)
		elif int(device["repair_status"])==5:
			subject = "Ремонт приладу завершено"
			message = get_template('email_templates/email_compleate_repair.html').render(vars)
		elif int(device["repair_status"])==6:
			subject = "Прилад відправлено"
			message = get_template('email_templates/email_delivery_repair.html').render(vars)
		elif int(device["repair_status"])==7:
			subject = "Відмова від ремонту"
			message = get_template('email_templates/email_stop_repair.html').render(vars)
		else:
			print("else")
		#sending email
		if int(device["repair_status"]) in [1,2,3,4,5,6,7]:
			msg = EmailMessage(
				subject, message, from_email=self.from_email,
				to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
				)
			msg.content_subtype = 'html'
			msg.mixed_subtype = 'related'
			msg.send()
			
	def send_pay_repair(self, device):
		target_emails = [device["custumer_email"]]

		vars = device
		if int(device["pay_repair_status"]):
			subject = "Статус оплати ремонту"
			message = get_template('email_templates/email_pay_repair.html').render(vars)
		else:
			print("else")
		#sending email
		if int(device["pay_repair_status"]):
			msg = EmailMessage(
				subject, message, from_email=self.from_email,
				to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
				)
			msg.content_subtype = 'html'
			msg.mixed_subtype = 'related'
			msg.send()

	def send_inform_repair(self, device):
		target_emails = [device["select_user_email"]]

		vars = device
		subject = "Інформація про стан ремонту обладнання"
		message = get_template('email_templates/email_inform_repair.html').render(vars)
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()
		
	def send_advertising_mail(self, device):
		target_emails =  device["email"]
		vars = device
		subject = "Медичне обладнання, інформація"
		message = get_template('email_templates/email_advertising_mail.html').render(vars)
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()

	#відправка електронного листа з даними клієнта який потребує технічну консультацію
	def send_help_repair(self, device):
		email = EMAIL_ADMIN
		target_emails = [email]

		vars = device
		subject = "Необхідна консультація"
		message = get_template('email_templates/email_need_consultation.html').render(vars)
		
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()

	#відправка електронного листа клієнту який відновлює пароль
	def email_recovery_password(self, new_password_info):
		target_emails = [new_password_info["email"]]

		vars = new_password_info
		subject = "Unimed.kiev.ua, відновлення паролю"
		message = get_template('email_templates/recovery_password.html').render(vars)
		
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()

	#відправка електронного листа клієнту який змінює пароль
	def email_change_password(self, new_password_info):
		target_emails = [new_password_info["email"]]

		vars = new_password_info
		subject = "Unimed.kiev.ua, зміна паролю"
		message = get_template('email_templates/change_password.html').render(vars)
		
		#sending email
		msg = EmailMessage(
			subject, message, from_email=self.from_email,
			to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails
			)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()


