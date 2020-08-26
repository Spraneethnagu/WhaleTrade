from django.conf.urls import url
from django.urls import path
from . import views

from .views import *



urlpatterns=[
    
    path('',views.index, name='index'),
    path('resources/',views.resources, name='resources')
    
]