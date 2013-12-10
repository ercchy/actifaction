from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, ButtonHolder, Layout


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		layout = Layout(
			Fieldset(_('Prijava'),
			         'username',
			         'password',
			         ),
			ButtonHolder(
				Submit('submit', _('Prijava'), css_class='btn btn-lg btn-primary btn-block'),
			),
		)

		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_tag = True
		self.helper.form_class = 'form-signin'
		self.helper.add_layout(layout)

