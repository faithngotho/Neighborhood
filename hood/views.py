from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as datetime
from .  forms import UserRegistrationForm,AddProjectForm,UserProjectForm,AddProjectForm
from . models import Project,Profile
from django.http import HttpResponse,Http404,HttpresponseRedirect


# Create your views here.
def welcome(request):
    return HttpResponse('Neighborhood')