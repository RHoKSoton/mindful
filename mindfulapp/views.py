from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from models import Patient,Carer
from utils import *

import sys

def index(request):
	return render_to_response('index.html')

def landing(request):
	if is_logged_in(request):
		if is_patient(request):
			return redirect('patient')
		else:
			return HttpResponse('You are logged in as a carer')
	else:
		return redirect('login_patient')

def login_patient(request):
  if request.method != "POST":
    patients = Patient.objects.all()
    return render_to_response('patientLogin.html', {'patients':patients})
  try:
    patient = Patient.objects.get(pk=request.POST['id'])
    request.session['loggedIn'] = True
    request.session['patient'] = patient
  except ObjectDoesNotExist:
    return HttpResponse('No login Information found for this person')
  return redirect('patient')

def login_carer(request):
	if request.method == "POST":
		email = request.POST['email']
		pwd = request.POST['password']
		try:
			carer = Carer.objects.get(email=email, password=pwd)
			request.session['loggedIn'] = True
			request.session['carer'] = carer
			return HttpResponse('YOU WOULD NOW BE TAKEN TO THE CARER SCREEN')
		except ObjectDoesNotExist:
				  return render_to_response('carerLogin.html', {'noUserFound':True})
	else:	
	  return render_to_response('carerLogin.html')

def logout(request):
   all_logout(request)
   return redirect('login_patient')

def patient(request):
    return HttpResponse('THIS IS THE PATIENT HOME SCREEN');
