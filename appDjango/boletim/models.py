from django.db import models

# Create your models here.
class Registrado(models.Model):
	nome = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    #def __str__(self): #Python 2
	#	return self.email

	def __str__(self): #Python 3
		return self.email
