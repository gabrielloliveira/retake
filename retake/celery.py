import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retake.settings')

app = Celery('retake', broker='redis://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_and_save_process_data': {
        'task': 'retake.core.tasks.get_and_save_process_data',
        'schedule': crontab(minute='*/2'),
        'args': (),
    },
}

app.autodiscover_tasks()
