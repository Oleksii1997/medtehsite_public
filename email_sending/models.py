from django.db import models


class EmailType(models.Model):
	email_type = models.CharField(max_length=128, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.email_type

	class Meta:
		verbose_name = "Тип листа: "
		verbose_name_plural = "Типи листів"

class EmailSending(models.Model):
	email_to = models.EmailField()
	email_type = models.ForeignKey(EmailType, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.email_to

	class Meta:
		verbose_name = "Відправлений лист: "
		verbose_name_plural = "Відправлені листи"