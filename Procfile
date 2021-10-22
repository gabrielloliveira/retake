worker: celery -A retake worker --loglevel=INFO
beat: celery -A retake beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: python manage.py runserver
