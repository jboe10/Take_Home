from django.db import models

# Create your models here.

Buisness_Choices = [('FS','Food Service'),('MS','Medical'),('CT','Construction'),('TE','Technology'),('SP','Sports'),('CL','Clothing')]

class Applicant(models.Model):

	Name 			= models.CharField(max_length=100)
	Amount_Required = models.IntegerField()
	Buisness_Type 	= models.CharField(choices = Buisness_Choices, default='Technology', max_length=100)
	Age 			= models.FloatField()

	class Meta:
		ordering = ('Name',)