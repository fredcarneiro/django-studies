from django.shortcuts import render
from profiles.models import Profile

def index(request):
	return render(request, 'index.html')

def show(request, profile_id):

	profile = Profile()

	if profile_id == '1':
		profile = Profile('Frederico Carneiro', 'carneiro@outlook.com', '77777777', 'Carneiro')

	return render(request, 'profile.html', {"profile": profile})
