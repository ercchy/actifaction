from django.db import models
from django import forms
from django.contrib.auth.models import User

class ActionCategory(models.Model):
	name = models.CharField(max_length=255) #we don't want to limit ourselves here, we'll rather do this in GUI
	slug = models.CharField(max_length=255)
	description = models.TextField(max_length=255,blank=True)

	def __unicode__ (self):
		return '%s' % (self.name)

class Action(models.Model):
	creation_date = models.DateField(auto_now_add = True)
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	description = models.TextField(max_length=255)
	action_date = models.DateTimeField()
	action_type = models.ForeignKey(ActionCategory)
	max_people = models.IntegerField(null=True,blank=True)
	#organizer = models.ForeignKey(User)


	def __unicode__ (self):
		return '%s' % (self.title)


