from django.db import models

class FacebookUser(models.Model):

	facebook_id = models.CharField(max_length=255,verbose_name="Id Facebook")
	name = models.CharField(max_length=255,verbose_name="Nombre de	usuario")
	link = models.CharField(max_length=255,verbose_name="URl de usuario")
	email = models.CharField(max_length=255,verbose_name="Email de	usuario")
	gender = models.CharField(max_length=255,verbose_name="Genero")
	birthday = models.DateField()
	created_date = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")

	class Meta:
		verbose_name = 'Usuario Facebook'
        verbose_name_plural = 'Usuarios de Facebook'

	def __unicode__(self):
		return self.name

