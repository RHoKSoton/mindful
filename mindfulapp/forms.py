from django import forms
from models import User

class ChooseUserForm(forms.Form):
    user = forms.ModelChoiceField(queryset = User.objects.all(), empty_label="Select a user")
