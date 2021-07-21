import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis import Myanalysis


def home(request):
    return render(request, 'index.html');

def d2(request):
    context = {'section':'d2.html'};
    return render(request, 'index.html',context);
def d3(request):
    context = {'section':'d3.html'};
    return render(request, 'index.html',context);


def check(request):
    context = {'section':'check.html'};
    return render(request, 'chart.html',context);
