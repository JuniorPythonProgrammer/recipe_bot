release: python manage.py migrate
web: gunicorn bot_admin.wsgi --log-file -
release: python manage.py bot