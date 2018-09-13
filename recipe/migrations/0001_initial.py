# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=200)),
                ('recipe_instructions', models.TextField()),
                ('recipe_author', models.CharField(max_length=200)),
                ('recipe_video', models.FileField(default=None, upload_to='uploads/')),
                ('recipe_rate', models.IntegerField(default=0)),
                ('recipe_feeds', models.CharField(max_length=200)),
                ('recipe_type', models.CharField(max_length=200)),
                ('recipe_category', models.CharField(max_length=200)),
                ('ingredient_amt', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('recipe_img', models.FileField(default=None, upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
    ]
