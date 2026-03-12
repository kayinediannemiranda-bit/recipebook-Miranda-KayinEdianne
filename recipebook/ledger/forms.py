from django import forms
from .models import RecipeIngredient, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'