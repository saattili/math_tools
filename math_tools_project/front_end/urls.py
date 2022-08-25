from django.urls import URLPattern,path

from . import views

fend_url_patterns = [
    path('',views.index,name='index'),
    path('prime_repeat/',views.prime_repeat,name='prime_repeat'),
]

# new_urls = [

#     path('',views.prime_repeat,name='prime_repeat'),
# ]