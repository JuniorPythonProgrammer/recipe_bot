from secrets import choice
from tabnanny import verbose
from django.db import models


class Profile(models.Model):
    MALE = 'чоловік'
    FEMALE = 'жінка'
    GENDER_CHOICES = [(MALE, 'Чоловік'), (FEMALE, 'Жінка')]

    REGISTRATION = 'RG'
    MAIN_MENU = 'MM'
    RECIPE_MENU = 'RM'
    USER_STATUS_CHOICES = [(REGISTRATION, 'Реєстрація'), (MAIN_MENU, 'Головне меню'), (RECIPE_MENU, 'Меню рецептів')]

    chat_id = models.IntegerField()
    user_name = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    user_status = models.CharField(
        max_length=2, 
        choices=USER_STATUS_CHOICES, 
        default=REGISTRATION
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(
        max_length=7, 
        choices=GENDER_CHOICES, 
        default=MALE
    )
    

class Recipe(models.Model):
    name_dish = models.CharField(max_length=250, unique=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    recipe = models.TextField()

    #def __str__(self):
    #    return self.name_dish
