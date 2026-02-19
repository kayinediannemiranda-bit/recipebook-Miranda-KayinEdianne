from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, Ingredient, RecipeIngredient

# def recipe_list_view(request):
#     recipe = RecipeIngredient.objects.all()
#     ingredients = RecipeIngredient.objects.all()
#     ctx = {
#         'recipe': recipe,
#         'ingredients': ingredients,
#     }
#     return render(request, "ledger/ledger_home_list.html", ctx
#     )

# def recipe_view(request):
#     recipe = RecipeIngredient.objects.all()
#     ingredients = RecipeIngredient.objects.all()
#     ctx = {
#         'recipe': recipe,
#         'ingredients': ingredients,
#     }
#     return render(request, "ledger/ledger_indiv_list.html", ctx
#     )

class TaskListView(ListView):
    model = RecipeIngredient
    template_name = 'ledger/ledger_home_list.html'

class TaskDetailView(DetailView):
    model = RecipeIngredient
    template_name = 'ledger/ledger_indiv_list.html'

