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
	contacts = models.ManyToManyField('self')

	def invite(self, invited_profile):
		invite = Invite(applicant=self, invited=invited_profile).save()

class Invite(models.Model):

	applicant = models.ForeignKey(Profile, related_name='made_invitations')
	invited = models.ForeignKey(Profile, related_name='received_invitations')
	
	def accept(self):
		self.invited.contacts.add(self.applicant)
		self.applicant.contacts.add(self.invited)
		self.delete()
		
		