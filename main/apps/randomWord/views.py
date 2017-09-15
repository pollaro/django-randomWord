from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    word = {'word':get_random_string(length=14)}
    if 'count' not in request.session or request.session['count'] == 0:
        request.session['count'] = 1
    return render(request,'randomWord/index.html',word)

def generate(request):
    if request.method == 'POST':
        request.session['count'] += 1
    return redirect(index)

def reset(request):
    request.session.clear()
    return redirect(index)
