from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from models import User
from utils import *

import sys

def index(request):
	return render_to_response('index.html')

def user(request, id):
	return render_to_response('user.html')

def carer(request, id):
	print id
	return render_to_response('carer.html')

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
  return redirect('user')

def login_carer(request):
  return HttpResponse('TODO login carer')

def logout(request):
   all_logout(request)
   return redirect('login_user')
