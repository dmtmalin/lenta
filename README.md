DJANGO_SETTINGS_MODULE=lenta.settings architect partition --module digest.models

python manage.py celery worker --loglevel=info
python manage.py celery beat --loglevel=info