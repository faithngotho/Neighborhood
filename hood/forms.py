from .models import Profile,Post,Neighbourhood,Business
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighbourhood']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood','pic','location')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','neighbourhood']