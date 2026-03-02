from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list_view(request, id):
    ctx = {
        'recipe': Recipe.object.get(pk=id)
    }
    return render(request, "ledger/ledger_home_list.html", ctx)

def recipe_view(request, id):
    ctx = {
        'recipe': Recipe.object.get(pk=id)
    }
    return render(request, "ledger/ledger_indiv_list.html", ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/ledger_home_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/ledger_indiv_list.html'
    redirect_field_name = 'ledger:recipe_list'

