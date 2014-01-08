from django import forms


class ActionForm(forms.Form):

    title = forms.CharField(max_length=100)
    location = forms.CharField()
    action_type = forms.CharField()
    max_participants = forms.IntegerField(required=True)
    description = forms.CharField()

