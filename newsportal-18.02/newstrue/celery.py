import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newstrue.settings')

app = Celery('newstrue')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()