from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello from home!</h1>')


def home_page(request):
    return render(request, 'home_page.html')