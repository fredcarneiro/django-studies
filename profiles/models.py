from django.db import models

class Profile_No_Models(object):

	def __init__(self, name='', email='', telephone='', company_name=''):
		self.name = name
		self.email = email
		self.telephone = telephone
		self.company_name = company_name

class Profile(models.Model):

	name = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	telephone = models.CharField(max_length=15, null=False)
	company_name= models.CharField(max_length=255, null=False)		
		