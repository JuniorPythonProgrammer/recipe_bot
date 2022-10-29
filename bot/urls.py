from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', menu, name='menu_url'),
    path('profiles/', profiles, name='profiles_url'),
    path('recipes/', recipes_list, name='recipes_list_url'),
    path('recipe/create/', RecipeCreate.as_view(), name='recipe_create_url'),
    path('recipe/<str:id>/update/', RecipeUpdate.as_view(), name='recipe_update_url'),
    path('recipe/<str:id>/delete/', RecipeDelete.as_view(), name='recipe_delete_url'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)