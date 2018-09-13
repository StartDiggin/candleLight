# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RecipeManager(models.Manager):
    def create_recipe(self, recipe_title, recipe_instructions, recipe_author, recipe_video, recipe_rate, recipe_feeds, recipe_type, recipe_category, recipe_img):
        recipe = self.create(
        recipe_title=recipe_title,
        recipe_instructions=recipe_instructions,
        recipe_author=recipe_author,
        recipe_video=recipe_video,
        recipe_rate=recipe_rate,
        recipe_feeds=recipe_feeds,
        recipe_type=recipe_type,
        recipe_category=recipe_category,
        recipe_img=recipe_img)
        return recipe

class IngredientManager(models.Manager):
    def add_ingredients(self, ingredient_name, ingredient_amt):
        ingredient = self.create(ingredient_name=ingredient_name, ingredient_amt=ingredient_amt)
        return ingredient

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_instructions = models.TextField()
    recipe_author = models.CharField(max_length=200)
    recipe_video = models.FileField(upload_to='uploads/', default=None)
    recipe_rate = models.IntegerField(default=0)
    recipe_feeds = models.CharField(max_length=200)
    recipe_type = models.CharField(max_length=200)
    recipe_category = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    recipe_img = models.FileField(upload_to='uploads/', default=None)
    objects = RecipeManager()
    def __str__(self):
        return self.recipe_title

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    ingredient_amt = models.CharField(max_length=200, default=None)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    objects = IngredientManager()
    def __str__(self):
        return self.ingredient_name
