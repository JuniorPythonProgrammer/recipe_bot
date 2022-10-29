release: python manage.py migrate
web: gunicorn bot_admin.wsgi --log-file -
web: gunicorn bot_admin.bot.managemends.commands.bot