from django.db import models

# this models for users authorisation the control 

class UsersAuthorisation(models.Model):
	username = models.CharField(max_length=24, blank=True, null=True, default=None)
	authorisation_status = models.BooleanField(default=False)
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.username

	class Meta:
		verbose_name = "Історія авторизацій користувач: "
		verbose_name_plural = "Історія авторизацій користувачів:"