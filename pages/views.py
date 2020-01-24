from django.shortcuts import render
from django.http import HttpResponse

#method that is gonna be used in urls.py
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')