from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=60)

	def __unicode__(self):
		return self.name

class Song(models.Model):
	title = models.CharField(max_length=100)
	artist = models.CharField(max_length=60)
	#file_name = models.CharField(max_length=100)
	length = models.IntegerField()	# in second
	bpm = models.IntegerField()		# beats per minute
	file = models.FileField(upload_to='mindfulapp/static/music')

	def delete(self, *args, **kwargs):
		# You have to prepare what you need before delete the model
		storage, path = self.file.storage, self.file.path
		# Delete the model before the file
		super(Song, self).delete(*args, **kwargs)
		# Delete the file after the model
		storage.delete(path)

	genre = models.ForeignKey(Genre)

	def __unicode__(self):
		return self.title

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	image = models.ImageField(upload_to='mindfulapp/static/users', null=True, blank=True)

	# songs = models.ManyToManyField(Song, null=True, blank=True)

	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

	def delete(self, *args, **kwargs):
		# You have to prepare what you need before delete the model
		storage, path = self.image.storage, self.image.path
		# Delete the model before the file
		super(User, self).delete(*args, **kwargs)
		# Delete the file after the model
		storage.delete(path)

	# TODO similar for update operation: old image has to be deleted

class Listen(models.Model):
	user_rating = models.DecimalField(decimal_places=2, max_digits=4)
	perc_listened = models.IntegerField()
	time_started = models.DateTimeField()
	time_ended = models.DateTimeField(null=True, blank=True)

	song = models.ForeignKey(Song)
	user = models.ForeignKey(User)

	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Carer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=60)
	password = models.CharField(max_length=30)

	# Many To Many Relationship between Carer and User
	users = models.ManyToManyField(User, null=True, blank=True)
	listens = models.ManyToManyField(Listen, through='Observation')
	
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Observation(models.Model):
	carer = models.ForeignKey(Carer)
	listen = models.ForeignKey(Listen)
	carer_rating = models.DecimalField(decimal_places=2, max_digits=4)
	notes = models.CharField(max_length=256)
	
