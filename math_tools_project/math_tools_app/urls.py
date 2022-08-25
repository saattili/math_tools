from . import views
from django.urls import URLPattern, path

url_patterns = [
    path('',views.prime_repeat,name='prime_repeat')
]