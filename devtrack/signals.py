from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Project, Feature, Sprint, FeatureGroup

@receiver(post_save, sender=User)
def create_featuregroup(sender, instance, created, **kwargs):
    if created:
        FeatureGroup.objects.create(sprint_project=instance)

@receiver(post_save, sender=User)
def create_sprint(sender, instance, created, **kwargs):
    if created:
        Sprint.objects.create(sprint_project=instance)

@receiver(post_save, sender=User)
def create_feature(sender, instance, created, **kwargs):
    if created:
        Feature.objects.create()
