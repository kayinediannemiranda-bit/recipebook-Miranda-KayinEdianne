from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list_view(request):
    recipe = RecipeIngredient.objects.all()
    ingredients = RecipeIngredient.objects.all()
    ctx = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, "ledger/ledger_home_list.html", ctx
    )

def recipe_view(request):
    recipe = RecipeIngredient.objects.all()
    ingredients = RecipeIngredient.objects.all()
    ctx = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, "ledger/ledger_indiv_list.html", ctx
    )

def task_detail(request, id):
    ctx = { 'recipe', 'ingredients', RecipeIngredient.objects.get(id=id) }
    return render(request, 'task_detail.html', ctx)

