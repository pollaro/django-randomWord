from django.shortcuts import render, redirect, HttpResponse
# from django.utils.crypto import get_random_string

def index(request):
    word = {'word':get_random_string(length=14)}
    return render(request,'index.html',word)

def reset(request):

    return redirect(index)
