from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageUpdateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/add_image', RecipeImageUpdateView.as_view(), name='recipe_detail'),
]

app_name = "ledger"