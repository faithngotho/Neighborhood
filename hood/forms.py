from .models import Profile,Post,Neighbourhood,Business
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighbourhood']

class UserRegistrationForm(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood','pic','location')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','neighbourhood']