from django import forms
from models import User, Observation

class ObservationForm(forms.ModelForm):

		class Meta:
				model = Observation
				fields = ('carer_rating','notes');
