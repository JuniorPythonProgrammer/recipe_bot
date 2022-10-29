from django import forms
from .models import Profile, Recipe


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['chat_id', 'user_name', 'first_name', 'last_name', 'user_status', 'name', 'gender']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name_dish', 'img', 'recipe']

        widgets = {
            'name_dish': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe': forms.Textarea(attrs={'class': 'form-control'}),
        }
