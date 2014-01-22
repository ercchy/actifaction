# -*- coding: utf-8 -*-
from django import forms
from django.utils.html import strip_tags
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from api.models import Action, ActionCategory

class ActionForm(forms.Form):

	title = forms.CharField(
		required=True, 
		label='Naslov akcije', 
		widget=forms.widgets.TextInput(),
		error_messages = {
			'required': u'Naslov je obvezen',
			'invalid': u'Preveri naslov',
		},
		)

	location = forms.CharField(
		required=True, 
		label='Lokacija', 
		widget=forms.widgets.TextInput(),
		error_messages = {
			'required': u'Kje se bo akcija dogajala?',
			'invalid': u'Preveri lokacijo',
		},
		)

	action_date = forms.CharField(
		required=True, 
		label='Datum', 
		widget=forms.widgets.TextInput(),
		error_messages = {
			'required': u'Kdaj bo akcija?',
			'invalid': u'Datum ni pravilno izpolnjen, uporabi koledar',
		},
		)

	action_type = forms.ModelChoiceField(
		required=True,
		label='Kategorija',
		widget=forms.widgets.Select(),
		queryset = ActionCategory.objects.all(),
		error_messages = {
			'required': u'Izberi eno izmed kategorij',
			'invalid': u'Preveri kategorijo',
		},
		)

	max_people = forms.IntegerField(
		label='Največje število udeležencev',
		required=False,
		min_value=1,
		widget=forms.widgets.NumberInput(),
		error_messages = {
			'invalid': u'Stevilka naj bo pozitivna',
		},
		)

	description = forms.CharField(
		required=True, 
		label='Opis', 
		widget=forms.widgets.Textarea(),
		error_messages = {
			'required': u'Kaj se bo dogajalo v okviru akcije?',
			'invalid': u'Preveri opis',
		},
		)


	def __init__(self, *args, **kwargs):
		super(ActionForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit','Dodaj', css_class='btn-primary'))

		self.helper.layout = Layout(
			Field("title","action_date","max_people","description","action_type","location",)
		)

	#class Meta:
	#	model = Action
	#	fields = ["title","location","action_date","action_type","max_people","description"]

	def is_valid(self):
		form = super(ActionForm, self).is_valid()
		for f,error in self.errors.iteritems():
			if f != '__all__':
				error=strip_tags(str(error))
				self.fields[f].widget.attrs.update({'class': 'error',})
		return form


