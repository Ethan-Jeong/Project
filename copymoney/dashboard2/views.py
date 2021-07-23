import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html');

def index2(request):
    return render(request, 'index2.html');

def index3(request):
    return render(request, 'index3.html');

def main_center(request):
    return render(request, 'main_center.html');

def check(request):
    context = {'section':'check.html'};
    return render(request, 'chart.html',context);
