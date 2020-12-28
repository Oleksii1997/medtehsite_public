from django.contrib import admin
from .models import *

class EmailTypeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EmailType._meta.fields]

	class Meta:
		model = EmailType

admin.site.register(EmailType, EmailTypeAdmin)

class EmailSendingAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EmailSending._meta.fields]

	class Meta:
		model = EmailSending

admin.site.register(EmailSending, EmailSendingAdmin)