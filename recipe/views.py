# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Recipe, Ingredient
from login.models import User

# Create your views here.
def index(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipe/index.html', context)

# Route to show recipes '/recipe'
def recipe(request):
    user_id = request.session['id']
    context = {
        'user': User.objects.get(pk=user_id),
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipe/recipe.html', context)

# Route to add Recipe page '/add_recipe'
def add_recipe(request):
    return render(request, 'recipe/add_recipe.html')

# Route to add Recipe '/addRecipe'
def addRrecipe(request):
    if 'recipe_id' in request.session:
        recipe_id = request.session['recipe_id']
        context = {
            'recipe': Recipe.objects.get(pk=recipe_id),
            'ingredients': Ingredient.objects.filter(recipe_id=recipe_id),
        }

        return render(request, 'recipe/add_recipe.html', context)
    else:

        return render(request, 'recipe/add_recipe.html')

# Route to create recipe 'createRecipe'
def createRecipe(request):
    user_id = request.session['id']
    user = User.objects.get(pk=user_id)
    print request.session['id']
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
    request.session['recipe_id'] = recipe.id
    return redirect('/addRrecipe')

# Route to add ingredients to recipe 'add_ingredients'
def ingredient(request):
    recipe_id = request.session['recipe_id']
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredient = Ingredient.objects.add_ingredients(ingredient_name=request.POST['ingredient_name'], ingredient_amt=request.POST['ingredient_amt'], recipe=recipe)
    return redirect('/addRrecipe')

# Route to show one recipe '/show/{{x.id}}'
def show_recipe(request, id):
    request.session['show_id'] = id
    recipe = Recipe.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(recipe__id=id)
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipe/showRecipe.html', context)

# Route to update Recipe '/updateRecipe/{{ recipe.id }}'
def update_recipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(recipe__id=id)
    context = {
        'recipe': recipe,
        'ingredients': ingredients,

    }
    return render(request, 'recipe/update_recipe.html', context)

# Route to update recipe '/update/{{recipe.id}}'
def update(request, id):
    recipe = Recipe.objects.get(pk=id)
    recipe.recipe_title = request.POST['recipe_title']
    recipe.recipe_instructions = request.POST['recipe_instructions']
    recipe.recipe_video = request.POST['recipe_video']
    recipe.recipe_rate = request.POST['recipe_rate']
    recipe.recipe_feeds = request.POST['recipe_feeds']
    recipe.recipe_type = request.POST['recipe_type']
    recipe.recipe_category = request.POST['recipe_category']
    recipe.recipe_img = request.POST['recipe_img']
    recipe.save()
    return redirect('/show/' + id)

# Route to update ingredient list '/updateIngredient/{{ recipe.id }}'
def updateIngredient(request, id):
    recipe = Recipe.objects.get(pk=id)
    ingredient = Ingredient.objects.add_ingredients(ingredient_name=request.POST['ingredient_name'], ingredient_amt=request.POST['ingredient_amt'], recipe=recipe)
    return redirect('/updateRecipe/' + id)

# Route to delete one ingredient '/delete/{{x.id}}'
def delete(request, id):
    ingredient = Ingredient.objects.get(pk=id).delete()
    return redirect('/addRrecipe')

# Route to delete one ingredient '/deleteRecipe/{{x.id}}'
def delete_recipe(request, id):
    Recipe.objects.get(pk=id).delete()
    return redirect('/recipe')

# Route to delete one ingredient from update page ''
def deleteIngredient(request, id):
    recipe_id = request.session['show_id']
    ingredient = Ingredient.objects.get(pk=id).delete()
    return redirect('/updateRecipe/' + recipe_id)
