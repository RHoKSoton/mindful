from django.db import models

# Create your models here.
class Patient(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name + self.last_name

class Genre(models.Model):
	name = models.CharField(max_length=60)

	def __unicode__(self):
		return self.name

class Song(models.Model):
	title = models.CharField(max_length=100)
	artist = models.CharField(max_length=60)
	file_name = models.CharField(max_length=100)
	length = models.IntegerField()	# in second
	bpm = models.IntegerField()		# beats per minute
	

	genre = models.ForeignKey(Genre)

	def __unicode__(self):
		return self.title

class Listen(models.Model):
	patient_rating = models.DecimalField(decimal_places=2, max_digits=4)
	perc_listened = models.IntegerField()
	time_started = models.DateTimeField()
	time_ended = models.DateTimeField()

	song = models.ForeignKey(Song)
	patient = models.ForeignKey(Patient)

	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Carer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=60)

	# Many To Many Relationship between Carer and Patient
	patients = models.ManyToManyField(Patient)
	listens = models.ManyToManyField(Listen, through='Observation')
	
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name + self.last_name

class Observation(models.Model):
	carer = models.ForeignKey(Carer)
	listen = models.ForeignKey(Listen)
	carer_rating = models.DecimalField(decimal_places=2, max_digits=4)
	notes = models.CharField(max_length=256)
