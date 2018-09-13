from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^recipe$', views.recipe),
url(r'^createRecipe$', views.createRecipe),
]
