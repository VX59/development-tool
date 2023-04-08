from django import forms
from django.contrib.auth.models import User
from .models import (Project, FeatureGroup, Feature, Bug, Sprint)

class FeatureAddForm(forms.Form):
    feature_group_choice = forms.ModelChoiceField(queryset=FeatureGroup.objects.all())
    feature_choice = forms.ModelChoiceField(queryset=Feature.objects.all())

class FeatureResolveForm(forms.Form):
    resolved = forms.BooleanField()