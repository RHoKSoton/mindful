from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return render_to_response('index.html')

def patient(request, id):
	print id
	return render_to_response('patient.html')
