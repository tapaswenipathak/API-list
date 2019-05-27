from django import forms
from main.models import Register

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ('email', 'phone_number')