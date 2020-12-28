from django.contrib import admin
from .models import *
# Register your models here.
class UsersAuthorisationAdmin(admin.ModelAdmin):
	list_display = [field.name for field in UsersAuthorisation._meta.fields]

	class Meta:
		model = UsersAuthorisation

admin.site.register(UsersAuthorisation, UsersAuthorisationAdmin)