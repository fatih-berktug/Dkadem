from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Game import api


app_name = "Game"

urlpatterns = [
    #path('', views.index, name='index'),
    # path('', views.login, name='login'),
    # path('forgot/', views.forgot, name='forgot'),

    url(r'permission/(?P<pk>\d+)$', views.permission, name='perm'),


]