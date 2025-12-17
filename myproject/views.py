# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hi, Coders... \n This is Home page...")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("HI Developers, \n This is About page for my Website...")
    return render(request, 'about.html')