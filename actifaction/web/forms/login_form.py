from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, ButtonHolder, Layout


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_tag = True
		self.helper.form_class = 'form-signin'
		self.helper.add_layout(Layout(
			Fieldset(_('Prijava'),
			         'username',
			         'password',
			),
			ButtonHolder(
				Submit('submit', _('Prijava'), css_class='btn btn-lg btn-primary btn-block'),
			),
		))

class RegisterForm(forms.Form):
	email = forms.EmailField(
		label = 'Email naslov',
		required = True,
		error_messages={
			'required': 'Vnesite email naslov',
			'invalid': 'Email naslov ni pravilen'
		}
	)
	
	password = forms.CharField(
		label = 'Geslo',
		max_length = 50,
		required = True,
		widget = forms.PasswordInput,
		)	


	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_tag = True
		self.helper.form_class = 'form-signin'
		self.helper.add_layout(Layout(
			Fieldset(_('Registracija'),
			         'email',
			         'password',
			),
			ButtonHolder(
				Submit('submit', _('Registracija'), css_class='btn btn-lg btn-primary btn-block'),
			),
		))