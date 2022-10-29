from re import T
from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot, types

from bot.models import Recipe, Profile
from bot.forms import ProfileForm


bot = TeleBot(settings.TOKEN, threaded=False)

def recipe_btn():
    recipes = Recipe.objects.all()
    btn = types.ReplyKeyboardMarkup()
    for recipe in recipes:
        name_dish_btn = types.KeyboardButton(recipe.name_dish)
        btn.row(name_dish_btn)
    mein_menu_btn = types.KeyboardButton('Повернутись до головного меню')
    btn.row(mein_menu_btn)
    return btn

def main_menu_btn():
    btn = types.ReplyKeyboardMarkup()
    about_user_btn = types.KeyboardButton('Про мене')
    recipe_btn = types.KeyboardButton('Рецепти')
    btn.row(about_user_btn, recipe_btn)
    return btn

def gender_btn():
    btn = types.ReplyKeyboardMarkup()
    gender_mele_btn = types.KeyboardButton('Чоловік')
    gender_femele_btn = types.KeyboardButton('Жінка')
    btn.row(gender_mele_btn, gender_femele_btn)
    return btn

def get_profile(message):
    profile = Profile.objects.get(chat_id=message.from_user.id)
    return profile

def update_status_prodile(profile, user_status):
    form = {'chat_id': profile.chat_id, 
        'user_name': profile.user_name, 
        'first_name': profile.first_name, 
        'last_name': profile.last_name, 
        'name': profile.name,
        'user_status': user_status,
        'gender': profile.gender
        }
    bound_form = ProfileForm(form, instance=profile)
    if bound_form.is_valid():
        update_prodile = bound_form.save()

def create_new_profile(message):
    from_user = {'chat_id': message.from_user.id, 
        'user_name': message.from_user.username, 
        'first_name': message.from_user.first_name, 
        'last_name': message.from_user.last_name, 
        'user_status': 'RG',
        'gender': 'чоловік'
        }
    bound_form = ProfileForm(from_user)
    if bound_form.is_valid():
        new_profile = bound_form.save()
    bot.send_message(message.chat.id, "Введіть своє ім'я")

def send_create_profile(message, profile):
    if profile.name == None:
        bot.send_message(message.chat.id, "Введіть своє ім'я")
    else:
        bot.send_message(message.chat.id, 'Виберіть свою стать', reply_markup=gender_btn())

def send_main_menu(message):
    bot.send_message(message.chat.id, 'Головне меню ', reply_markup=main_menu_btn())

def send_recipes_menu(message):
    bot.send_message(message.chat.id, 'Меню рецептів', reply_markup=recipe_btn())
    

def create_profile(message, profile):
    if profile.name == None:
        message_user = {'chat_id': message.from_user.id, 
            'user_name': message.from_user.username, 
            'first_name': message.from_user.first_name, 
            'last_name': message.from_user.last_name, 
            'user_status': 'RG',
            'name': message.text,
            'gender': 'чоловік'
        }
        bound_form = ProfileForm(message_user, instance=profile)
        if bound_form.is_valid():
            update_profile = bound_form.save()
            send_create_profile(message, profile)
        else:
            bot.send_message(message.chat.id, 'Помилка')
    else:
        message_user = {'chat_id': message.from_user.id, 
            'user_name': message.from_user.username, 
            'first_name': message.from_user.first_name, 
            'last_name': message.from_user.last_name, 
            'name': profile.name,
            'user_status': 'MM',
            'gender': message.text.lower()
        }
        bound_form = ProfileForm(message_user, instance=profile)
        if bound_form.is_valid():
            new_profile = bound_form.save()
            bot.send_message(message.chat.id, 'Дякую за реєстрацію')
            send_main_menu(message)
        else:
            bot.send_message(message.chat.id, 'Виберіть із списку')

def main_menu(message, profile):
    if message.text.lower() == 'про мене':
        bot.send_message(message.chat.id, f"Ваше ім'я: {profile.name} \nВаша стать: {profile.gender}")
    elif message.text.lower() == 'рецепти':
        update_status_prodile(profile, user_status='RM')
        send_recipes_menu(message)

def recipes_menu(message, profile):
    if message.text.lower() == 'повернутись до головного меню':
        update_status_prodile(profile, user_status='MM')
        send_main_menu(message)
    else:
        recipes = Recipe.objects.all()
        recipe_existence = False
        for recipe in recipes:
            if recipe.name_dish==message.text:
                recipe_existence = True

        if recipe_existence:
            recipe = Recipe.objects.get(name_dish__iexact=message.text)
            if recipe.img:
                bot.send_photo(message.chat.id, recipe.img)
            bot.send_message(message.chat.id, recipe.recipe)
        else:
            bot.send_message(message.chat.id, 'Такого рецепта немає')


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()


@bot.message_handler(commands=['start'])
def welcome(message):
    profiles = Profile.objects.all()
    profile_existence = False
    for profile in profiles:
        if profile.chat_id==message.from_user.id:
            profile_existence = True
            break

    if profile_existence == False :
        bot.send_message(message.chat.id, "Вас вітає бот рецептів")
        create_new_profile(message)
    else:
        profile = get_profile(message)
        if profile.user_status == 'RG':
            send_create_profile(message, profile)
        elif profile.user_status == 'MM':
            send_main_menu(message)
        elif profile.user_status == 'RM':
            send_recipes_menu(message)


@bot.message_handler(content_types = ['text'])
def receive_text(message):
    profile = get_profile(message)
    if profile.user_status == 'RG':
        create_profile(message, profile)
    elif profile.user_status == 'MM':
        main_menu(message, profile)
    elif profile.user_status == 'RM':
        recipes_menu(message, profile)

