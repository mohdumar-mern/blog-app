# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hi, Coders... \n This is Home page...")
    return render(request, 'home.html')
