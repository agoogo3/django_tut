from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    template = loader.get_template('members.html')
   
    return HttpResponse(template.render())
