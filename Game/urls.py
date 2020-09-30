from django.conf.urls import url
from django.urls import path, include
from Game import ViewController
app_name = "Game"

urlpatterns = [
    path('',ViewController.main, name='index'),



]