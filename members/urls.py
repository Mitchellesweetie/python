from django.urls import path
from . import views

urlpatterns=[
    path('',views.members,name='members'),
    path('counter',views.counter,name='counter')
]