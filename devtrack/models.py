from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk' : self.pk})

class Sprint(models.Model):
    active = models.BooleanField(default=False)
    sprint_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sprint_name = models.CharField(max_length=16)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=timezone.now())
    days = models.IntegerField(default=5)
    def get_all_issues(self):
        issues = 0
        for f in self.feature_set.all():
            issues += f.bug_set.count()
        return issues
    
    def get_all_resolved(self):
        resolved = 0
        for f in self.feature_set.all():
            if f.resolved: resolved += 1
        return resolved

    def get_unresolved_instances(self):
        return self.feature_set.all().filter(resolved=False)
    
    def get_resolved_instances(self):
        return self.feature_set.all().filter(resolved=True)

    def get_all_progress(self):
        progress = 0
        for f in self.feature_set.all():
            if f.in_progress: progress += 1
        return progress

    def __str___(self):
        return self.sprint_name

    def get_absolute_url(self):
        return reverse('sprint-detail', kwargs={'pk' : self.pk})

class FeatureGroup(models.Model):
    project_parent = models.ForeignKey(Project, on_delete=models.CASCADE)
    category_date_created = models.DateTimeField(default=timezone.now)
    category_name = models.CharField(max_length=32)
    category_description = models.TextField(default='')
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk' : self.pk})
    
    def get_unresolved_instances(self):
        return self.feature_set.all().filter(resolved=False)
    
    def get_resolved_instances(self):
        return self.feature_set.all().filter(resolved=True)

class FeaturePriority(models.IntegerChoices):
    HIGH = 1, 'HIGH'
    MODERATE = 2, 'MODERATE'
    LOW = 3, 'LOW'

class Feature(models.Model):
    sprint_active = models.BooleanField(default=False)  
    resolved = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    category_parent = models.ForeignKey(FeatureGroup, on_delete=models.CASCADE, null=True)
    feature_date_created = models.DateTimeField(default=timezone.now)
    feature_name = models.CharField(max_length=32)
    feature_description = models.TextField(default='')
    priority = models.IntegerField(default=FeaturePriority.HIGH, choices=FeaturePriority.choices)

    def __str__(self):
        return self.feature_name

    def resolve(self):
        self.resolved = True
        print(self.id)
        self.save()

    def get_absolute_url(self):  # return full path of a post instace
        return reverse('feature-detail', kwargs={'pk' : self.pk})

class BugSeverity(models.IntegerChoices):
    SEVERE = 1, 'SEVERE'
    MODERATE = 2, 'MODERATE'
    WARNING = 3, 'WARNING'

class Bug(models.Model):
    feature_parent = models.ForeignKey(Feature, on_delete=models.CASCADE)
    bug_date_created = models.DateTimeField(default=timezone.now)
    bug_name = models.CharField(max_length=32)
    severity = models.IntegerField(default=BugSeverity.MODERATE, choices=BugSeverity.choices)
    terminal_feedback = models.TextField(default='')

    def __str__(self):
        return self.bug_name

    def get_absolute_url(self):
        return reverse('bug-detail', kwargs={'pk' : self.pk}) 
