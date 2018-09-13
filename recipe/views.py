# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Recipe, Ingredient
from login.models import User

# Create your views here.
def index(request):
    return render(request, 'recipe/index.html')

def recipe(request):
    return render(request, 'recipe/recipe.html')

def createRecipe(request):
    user = User.objects.get(pk=1)
    recipe = Recipe.objects.create_recipe(
    recipe_title = request.POST['recipe_title'],
    recipe_instructions = request.POST['recipe_instructions'],
    recipe_author = user,
    recipe_video = request.POST['recipe_video'],
    recipe_rate = request.POST['recipe_rate'],
    recipe_feeds = request.POST['recipe_feeds'],
    recipe_type = request.POST['recipe_type'],
    recipe_category = request.POST['recipe_category'],
    recipe_img = request.POST['recipe_img']
    )

    print user
    return redirect('/recipe')
