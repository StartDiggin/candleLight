from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^recipe$', views.recipe),
url(r'^add_recipe$' , views.add_recipe),
url(r'^addRrecipe$', views.addRrecipe),
url(r'^createRecipe$', views.createRecipe),
url(r'^add_ingredients$', views.ingredient),
url(r'^delete/(?P<id>\d+)$', views.delete),
url(r'^deleteRecipe/(?P<id>\d+)$', views.delete_recipe),
url(r'^show/(?P<id>\d+)$', views.show_recipe),
url(r'^updateRecipe/(?P<id>\d+)$', views.update_recipe),
url(r'^update/(?P<id>\d+)$', views.update),
url(r'^updateIngredient/(?P<id>\d+)$', views.updateIngredient),
url(r'^deleteIngredient/(?P<id>\d+)$', views.deleteIngredient),
]
# <a href="/cards/show/{{card.id}}">show</a>
# url(r'^show/(?P<id>\d+)$',views.show),
