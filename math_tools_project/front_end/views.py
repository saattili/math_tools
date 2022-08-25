from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def prime_repeat(request):
    return render(request,'prime_repeat.html')

