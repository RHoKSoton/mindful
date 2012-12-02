from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from models import User, Carer, Listen
from forms import ChooseUserForm
from utils import *

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

def user(request, id):
	return render(request, 'user.html')

def carer(request, id):
	carer = Carer.objects.get(pk=id)
	return render(request, 'carer.html', {'carerid':id, 'users':carer.users.all})

def view_user(request, carer_id, user_id):
	return HttpResponse('Viewing user '+user_id);

def login_user(request):
  if request.method != "POST":
    users = User.objects.all()
    return render_to_response('userLogin.html', {'users':users})
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
				  return render_to_response('carerLogin.html', {'noUserFound':True})
	else:	
	  return render_to_response('carerLogin.html')

def logout(request):
   all_logout(request)
   return redirect('login_user')
