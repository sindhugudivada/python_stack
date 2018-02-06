from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.


def index(request):
    return render(request, 'surveys/index.html')


def display_result(request):
    return render(request, 'surveys/success.html')


def getinfo(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    if request.method == "POST":
        request.session['number'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
