from django.urls import path
from Game.viewController import ViewController

app_name = "Game"

urlpatterns = [
    path('', ViewController.main, name='index'),



]