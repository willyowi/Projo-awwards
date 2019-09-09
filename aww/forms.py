from django import forms
from aww.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','timestamp']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile','timestamp']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user','project','average']
