from django.db import models

class Profile(object):

	def __init__(self, name='', email='', telephone='', company_name=''):
		self.name = name
		self.email = email
		self.telephone = telephone
		self.company_name = company_name
		