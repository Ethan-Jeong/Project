import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis import Myanalysis

def home(request):
    return render(request, 'loading.html');

def index(request):
    return render(request, 'index.html');

def index2(request):
    return render(request, 'index.html');

def loading(request):
    return render(request, 'loading.html');

def loading3(request):
    return render(request, 'loading3.html');

def coin(request):
    data = Myanalysis.Project().coin();
    return HttpResponse(json.dumps(data), content_type='application/json', many=True);