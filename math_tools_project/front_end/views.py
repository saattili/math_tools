from django.shortcuts import render

import json

def index(request):
    return render(request,'index.html')


def prime_repeat(request):
    if request.method == "POST":
        res = request.POST
        data = dict(res)
        set_value = data['prime_num'][0]
        print()
        #print(data.csrfmiddlewaretoken)
        return render(request,'prime_repeat.html',{
            'value': set_value,
        })

    return render(request,'prime_repeat.html')

