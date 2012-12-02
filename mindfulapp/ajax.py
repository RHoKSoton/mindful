from django.utils import simplejson
from django.core import serializers
from dajaxice.decorators import dajaxice_register
from models import User, Carer, Listen

@dajaxice_register
def sayhello(request):
	return simplejson.dumps({'message':'Hello World'})

@dajaxice_register
def getlisteners(request, carerid):
	carer = Carer.objects.get(pk=carerid)
	listeners = Listen.objects.filter(
		user__in=carer.users.all
	).filter(
		time_ended__isnull=True
	)
	results = []
	for listener in listeners:
		results.append({'id': listener.id, 'first_name':listener.user.first_name, 'name' : listener.user.name(), 'song' : listener.song.title})
	return simplejson.dumps(results)



