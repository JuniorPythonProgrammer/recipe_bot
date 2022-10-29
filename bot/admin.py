from django.contrib import admin

from .models import Profile, Recipe

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'user_name', 'first_name', 'last_name', 'user_status', 'name', 'gender']
    list_editable = ['chat_id', 'user_name', 'first_name', 'last_name', 'user_status', 'name', 'gender']

admin.site.register(Profile, ProfileAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_dish', 'img', 'recipe']
    list_editable = ['name_dish', 'img', 'recipe']

admin.site.register(Recipe, RecipeAdmin)
