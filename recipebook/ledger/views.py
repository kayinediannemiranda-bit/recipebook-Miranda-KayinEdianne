from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/ledger_home_list.html'
    

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/ledger_indiv_list.html'
    redirect_field_name = 'ledger:recipe_list'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/ledger_form.html'
    form_class = RecipeForm


class RecipeAddImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'ledger/ledger_form_addimage.html'
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk': self.object.recipe.id})

