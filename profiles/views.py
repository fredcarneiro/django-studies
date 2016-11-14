from django.shortcuts import render, redirect
from profiles.models import Profile, Invite

def index(request):
	return render(request, 'index.html', {'profiles': Profile.objects.all(), "logged_profile": get_logged_profile(request)})

def show(request, profile_id):
	
	logged_profile = get_logged_profile(request)
	profile = Profile.objects.get(id=profile_id)
	
	is_contact = profile in logged_profile.contacts.all()
	

	return render(request, 'profile.html', {"profile": profile, "is_contact": is_contact, "logged_profile": logged_profile})

def invite(request, profile_id):
	profile_to_invite = Profile.objects.get(id=profile_id)
	logged_profile = get_logged_profile(request)

	logged_profile.invite(profile_to_invite)

	return redirect('index')
	
def accept_invitation(request, invitation_id):
	
	invitation = Invite.objects.get(id=invitation_id)
	invitation.accept()
	
	return redirect('index')
	

def get_logged_profile(request):
	return Profile.objects.get(id=2)
