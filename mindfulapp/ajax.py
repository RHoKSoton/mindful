from django.utils import simplejson
from django.core import serializers
from dajaxice.decorators import dajaxice_register
from models import User, Carer, Listen
from datetime import datetime

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
		results.append({'id': listener.id, 'name' : listener.user.name(), 'song' : listener.song.title})
	return simplejson.dumps(results)

@dajaxice_register
def updaterating(request, listenId, rating):
	listen = Listen.objects.get(pk=listenId)
	listen.user_rating = rating
	listen.save()

@dajaxice_register
def setFinishTime(request, listenId):
	listen = Listen.objects.get(pk=listenId)
	listen.time_ended = datetime.now()
	listen.save()




