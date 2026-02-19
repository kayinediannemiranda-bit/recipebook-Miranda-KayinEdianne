from django.urls import path

from .views import recipe_list_view, recipe_view

urlpatterns = [
    path('recipes/list', recipe_list_view, name='recipe_list_view'),
    path('recipe/1', recipe_view, name='recipe_view'),
]

app_name = "ledger"