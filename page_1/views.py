from django.shortcuts import render
from django.http import HttpResponse


def page_1(request):
    return HttpResponse('<h1>Hello from page_1!</h1>')
