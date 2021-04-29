
from django.urls import path

from .views import home, about, contact, blog 

urlpatterns = [
    path('',  home, name="home"),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog')
]
