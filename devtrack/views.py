from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Project, Feature, Bug, Sprint, FeatureGroup
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django import forms
from django.utils.safestring import mark_safe
from .utils import Calendar
from datetime import datetime
from .forms import FeatureAddForm, FeatureResolveForm


def home(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'home.html', context)

class ProjectListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Project
    template_name = 'devtrack/home.html'
    context_object_name = 'projects'
    paginate_by = 5

    '''def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_created')'''

class ProjectDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Project
    template_name = 'devtrack/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        cal = Calendar(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()

class ProjectCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Project
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Project
    fields = ['title', 'description']
    template_name = 'devtrack/project_update.html'
    context_object_name = 'project_update'

    def form_valid(self, form):
        form.save()
        form.instance.author = self.request.user
        messages.success(self.request, f'Your project has been updated')
        return super().form_valid(form)

class ProjectEditView(DetailView):
    model = Project
    template_name = 'devtrack/project_edit.html'
    context_object_name = 'project_edit'

class FeatureGroupCreateView(CreateView):
    model = FeatureGroup
    template_name = 'devtrack/group_create.html'
    context_object_name = 'group-create'
    fields = ['project_parent','category_name', 'category_description']

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Your group has been updated')
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('group-edit', kwargs={'pk' : self.object.pk})

class FeatureGroupDetailView(DetailView):
    model = FeatureGroup
    template_name = 'devtrack/group_detail.html'
    context_object_name = 'group_details'

class FeatureGroupEditView(DetailView):
    model = FeatureGroup
    template_name = 'devtrack/group_edit.html'
    context_object_name = 'project_group_edit'

class FeatureGroupListView(ListView):
    model = FeatureGroup
    template_name = 'devtrack/project_detail.html'
    context_object_name = 'feature_group'

class FeatureCreateView(CreateView):
    model = Feature
    template_name = 'devtrack/feature_create.html'
    context_object_name = 'feature_create'
    fields = ['category_parent', 'feature_name', 'feature_description', 'priority']
    widget = {'category_parent': forms.HiddenInput()}
    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'You have added a feature')
        return super().form_valid(form)

class FeatureUpdateView(UpdateView):
    model = Feature
    template_name = 'devtrack/feature_update.html'
    context_object_name = 'feature_update'
    fields = ['category_parent', 'feature_name', 'feature_description', 'priority']
    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'You have updated a feature')
        return super().form_valid(form)

class FeatureListView(ListView):
    model = Project
    template_name = 'devtrack/project_detail.html'
    context_object_name = 'project_features'

class FeatureDetailView(DetailView):
    model = Feature
    template_name = 'devtrack/feature_detail.html'
    context_object_name = 'feature_details'

def AddFeature(request, pk):
    if request.method == 'POST':
        sprint = get_object_or_404(Sprint, id=pk)
        form = FeatureAddForm(request.POST)
        if form.is_valid():
            feature = form.cleaned_data.get('feature_choice')
            feature.sprint = sprint
            feature.sprint_active = True
            feature.save()
            messages.success(request, f'You have added a feature')
            return redirect('sprint-edit', pk)
    else:
        form = FeatureAddForm()
    
    return render(request, 'devtrack/feature_add.html', {'form' : form})

def ResolveFeatureView(request, pk):
    if request.method == 'POST':
        feature = get_object_or_404(Sprint, id=pk)
        form = FeatureResolveForm(request.POST)
        if form.is_valid():
            resolved = form.cleaned_data.get('resolved')
            feature.resolved = resolved
            feature.save()
            messages.success(request, f'You have resolved a feature')
            return redirect('sprint-edit', pk)
    else:
        form = FeatureResolveForm()
    
    return render(request, 'devtrack/feature_resolve.html', {'form' : form})

class BugDetailView(DetailView):
    model = Bug
    template_name = 'devtrack/bug_detail.html'
    context_object_name = 'bug_details'

class SprintCreateView(CreateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Sprint
    template_name = 'devtrack/sprint_create.html'
    context_object_name = 'sprint_create'
    fields = ['sprint_project', 'sprint_name', 'start_date', 'end_date', 'days']

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'You have created a sprint')
        return super().form_valid(form)

class SprintDetailView(DetailView):
    model = Sprint
    template_name = 'devtrack/sprint_detail.html'
    context_object_name = 'sprint_details'

class SprintEditView(DetailView):
    model = Sprint
    template_name = 'devtrack/sprint_edit.html'
    context_object_name = 'sprint_edit'

class CalendarView(ListView):
    model = Sprint
    template_name = 'devtrack/project_detail.html'
    context_object_name = 'calendar'