from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(validators=[
            MinLengthValidator(50, 'Bio must contain at least 255 characters')
            ])

    def __str__(self):
        return self.user.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
    

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.id)])#try self.id and 'ledger:recipe_detail'


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name= 'recipe_image')

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.recipe.id)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    
    class Meta: 
        ordering = ['recipe']
        verbose_name = 'recipeingredient'
        verbose_name_plural = 'recipeingredients'