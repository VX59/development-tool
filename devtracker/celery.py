import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtracker.settings')

app = Celery('devtracker')
app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()

@app.task(bint=True)
def debug_task(self):
    print(f'Request: {self.request!r}')