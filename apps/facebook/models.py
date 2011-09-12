from django.db import models

class FacebookUser(models.Model):

	facebook_id = models.CharField(max_length=255,verbose_name="Id Facebook")
	username = models.CharField(max_length=255,verbose_name="Nombre de	usuario")
	email = models.CharField(max_length=255,verbose_name="Email de	usuario")
	gender = models.CharField(max_length=255,verbose_name="Genero")
	birthday = models.DateField()
	created_date = models.DateTimeField(auto_now_add=True)

