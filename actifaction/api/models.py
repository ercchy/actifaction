from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.html import strip_tags

class ActionCategory(models.Model):
    name = models.CharField(max_length=20)
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
    max_people = models.IntegerField(blank=True)
    organizer = models.ForeignKey(User)


    def __unicode__ (self):
		return '%s' % (self.title)


class ActionForm(forms.ModelForm):
    title = forms.CharField(required=True, label='Naslov akcije', widget=forms.widgets.TextInput())
    location = forms.CharField(required=True, label='Lokacija', widget=forms.widgets.TextInput())
    action_date = forms.CharField(required=True, label='Naslov akcije', widget=forms.widgets.TextInput())


    class Meta:
        model = Action
        fields = ["title","location","action_date","action_type","max_people","description"]

    def is_valid(self):
        form = super(ActionForm, self).is_valid()
        for f,error in self.errors.iterkeys():
            if f != '__all__':
                error=strip_tags(str(error))
                self.fields[f].widget.attrs.update({'class': 'error', 'value': error})
        return form


