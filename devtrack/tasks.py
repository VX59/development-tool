from .models import Feature
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def count_objects():
    return Feature.objects.count()

@shared_task
def rename_object(obj, id, name):
    w = obj.objects.get(id=id)
    w.name = name
    w.save()