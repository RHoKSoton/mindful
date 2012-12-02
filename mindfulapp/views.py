from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


from models import User, Carer, Listen, Observation, Song
from forms import ObservationForm
from random import choice
from django.db.models import Avg
from utils import *
from datetime import datetime

import sys

def index(request):
	return render_to_response('index.html')

def landing(request):
	if is_logged_in(request):
		if is_user(request):
			return redirect('user', request.session['user'].id)
		else:
			return redirect('carer', request.session['carer'].id)
	else:
		return redirect('login_user')

def user_play(request, id):
	# Get songs
	songs = Song.objects.all()
	# get songs with best average
	listens = Listen.objects.values('song').annotate(avg=Avg('user_rating')).order_by('-avg')

	listens = listens[:5]

	# select one randomly, get the id, do a lookup in SONG, get path

	from random import choice
	listens = choice(listens)

	song_id = listens['song']

	play_song = Song.objects.get(id = song_id)

	# extract file name
	path = play_song.file.path
	filename = path[(path.rfind('/')+1):]


	# Create new listen object
	currentUser = User.objects.get(id = 1)
	newListen = Listen(user_rating = 5, perc_listened = 100, time_started = datetime.now(), song = play_song, user = currentUser)
	newListen.save()

	return render(request, 'user_play.html', {'filename':filename, 'listenId':newListen.id})

def carer(request, id):
	carer = Carer.objects.get(pk=id)
	return render(request, 'carer.html', {'carerid':id, 'users':carer.users.all})

def user(request, id):
  return HttpResponse('You are signed in as a user')

def view_user(request, carer_id, user_id):
	user = User.objects.get(pk=user_id)
	listens = Listen.objects.filter(
		user_id = user_id
	).order_by(
		'-added'
	)
	observations = Observation.objects.filter(
			carer_id = carer_id
	).filter(
			listen__in = listens
	)
	return render(request, 'carerUserProfile.html', {'listens':listens, 'user':user, 'observations':observations, 'carerid':carer_id})

def observation(request, carerid, listenid):
	try:
		observation = Observation.objects.get(carer_id = carerid, listen_id = listenid)	
	except ObjectDoesNotExist:
		observation = Observation(carer_id = carerid, listen_id = listenid)
	if request.method == "POST":
		form = ObservationForm(request.POST, instance = observation)
		form.save()
		return redirect('view_user', carerid, observation.listen.user.id);
	else:
		form = ObservationForm(instance = observation)
		return render(request, 'observation.html', {'form':form})

def login_user(request):
  if request.method != "POST":
    users = User.objects.all()
    return render(request, 'userLogin.html', {'users':users})
  try:
    user = User.objects.get(pk=request.POST['id'])
    request.session['loggedIn'] = True
    request.session['user'] = user
  except ObjectDoesNotExist:
    return HttpResponse('No login Information found for this person')
  return redirect('user', user.id)

def login_carer(request):
	if request.method == "POST":
		email = request.POST['email']
		pwd = request.POST['password']
		try:
			carer = Carer.objects.get(email=email, password=pwd)
			request.session['loggedIn'] = True
			request.session['carer'] = carer
			return redirect('carer', carer.id)
		except ObjectDoesNotExist:
				  return render(request, 'carerLogin.html', {'noUserFound':True})
	else:	
	  return render(request, 'carerLogin.html')

def logout(request):
   all_logout(request)
   return redirect('login_user')
