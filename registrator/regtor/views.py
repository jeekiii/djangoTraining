from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, id_image):
    return render(request, 'regtor/home.html', locals())
