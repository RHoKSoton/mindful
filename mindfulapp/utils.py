def is_patient(request):
  return request.session['patient'] != NULL

def is_carer(request):
  return request.session['carer'] != NULL

def is_logged_in(request):
  return request.session['loggedIn'] != NULL

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
