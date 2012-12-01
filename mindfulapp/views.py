from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from models import Patient
from utils import *

import sys

def index(request):
	return render_to_response('index.html')

<<<<<<< HEAD
def patient(request, id):
	print id
	return render_to_response('patient.html')
=======
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
  return HttpResponse('TODO login carer')

def logout(request):
   all_logout(request)
   return redirect('login_patient')

def patient(request):
    return HttpResponse('THIS IS THE PATIENT HOME SCREEN');
>>>>>>> 601ac51b8510f656ddeac3099e29c935daee7b80
