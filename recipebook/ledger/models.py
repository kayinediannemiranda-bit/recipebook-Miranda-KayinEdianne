from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])

class RecipeIngridient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes')
    
    class Meta: 
        ordering = ['recipe']
        verbose_name = 'recipeingridient'
        verbose_name_plural = 'recipeingridients'