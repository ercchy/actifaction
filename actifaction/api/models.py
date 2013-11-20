from django.db import models

class Action(models.Model):
	creation_date = models.DateField()
	title = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	action_date = models.DateTimeField()
	action_type = models.IntegerField()

	def __unicode__ (self):
		return '%s' % (self.title)