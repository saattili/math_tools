from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def prime_repeat(request):
    return HttpResponse("Hi This is the first Page")
