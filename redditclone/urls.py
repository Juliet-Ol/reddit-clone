from django.urls import path
from . import views
from redditclone import views


urlpatterns = [
    path('', views.index, name='index'),
]