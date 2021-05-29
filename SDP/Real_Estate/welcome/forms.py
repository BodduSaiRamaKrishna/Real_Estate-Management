from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class DetailsForm(ModelForm):
	class Meta:
		model = Details
		fields='__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class FeedbackForm(ModelForm):
	class Meta:
		model=Feedback
		fields=['fname','lname','country']

class ImageForm(forms.ModelForm):
	class Meta:
		model=Image
		fields=("caption","image")


class TranForm(forms.ModelForm):
	class Meta:
		model= Tran
		fields=['fname','email','add','city','state','zip','cname','cnum','expmonth','expyear','cvv']