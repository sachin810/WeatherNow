from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.weatherview, name='index'),

]