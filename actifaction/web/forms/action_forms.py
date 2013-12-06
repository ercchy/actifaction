from django import forms
from django.utils.html import strip_tags
from api.models import Action

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


