from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^createUser$', views.create),
    url(r'^login$', views.login),
    url(r'^speech$', views.speech),
]
