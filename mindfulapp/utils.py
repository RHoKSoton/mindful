def is_patient(request):
	return 'patient' in request.session

def is_carer(request):
	return 'carer' in request.session

def is_logged_in(request):
	return 'loggedIn' in request.session

def all_logout(request):
  try:
    del request.session['loggedIn']
  except KeyError:
        pass
  try:
    del request.session['patient']
  except KeyError:
        pass
  try:
    del request.session['carer']
  except KeyError:
        pass
