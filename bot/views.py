from django.shortcuts import redirect, render
from django.views.generic import View
from django.urls import reverse

from .models import Profile, Recipe
from .forms import RecipeForm

def menu(request):
    return render(request, 'admin/menu.html')

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'admin/profiles.html', context={'profiles': profiles})

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'admin/recipes_list.html', context={'recipes': recipes})

class RecipeCreate(View):
    def get(self, request):
        form = RecipeForm()
        return render(request, 'admin/recipe_create.html', context={'form': form})

    def post(self, request):
        bound_form = RecipeForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_recipe = bound_form.save()
            return redirect(reverse('recipes_list_url'))
        return render(request, 'admin/recipe_create.html', context={'form': bound_form})

class RecipeUpdate(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        bound_form = RecipeForm(instance=recipe)
        return render(request, 'admin/recipe_update.html', context={'form': bound_form,'recipe': recipe})

    def post(self, request, id):
        recipe = Recipe.objects.get(id=id)
        bound_form = RecipeForm(request.POST, request.FILES ,instance=recipe)

        if bound_form.is_valid():
            update_recipe = bound_form.save()
            return redirect(reverse('recipes_list_url'))
        return render(request, 'admin/recipe_update.html', context={'form': bound_form, 'recipe': recipe})

class RecipeDelete(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        return render(request, 'admin/recipe_delete.html', context={'recipe': recipe})
        
    def post(self, request, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return redirect(reverse('recipes_list_url'))
