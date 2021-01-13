from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class ProfileModelForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'bio', 'image')