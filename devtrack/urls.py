from django.urls import path
from .views import (ProjectListView, ProjectDetailView, ProjectCreateView,
                    FeatureCreateView, FeatureDetailView, BugDetailView,
                    SprintDetailView, ProjectEditView, ProjectUpdateView,
                    SprintEditView, FeatureGroupEditView, FeatureUpdateView,
                    SprintCreateView, FeatureGroupCreateView, FeatureGroupDetailView,
                    AddFeature, ResolveFeatureView)

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/edit/', ProjectEditView.as_view(), name='project-edit'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/group/<int:pk>/', FeatureGroupEditView.as_view(), name='group-edit'),
    path('project/group/feature<int:pk>/update', FeatureUpdateView.as_view(), name='feature-update'),
    path('project/group/<int:pk>/features/create/', FeatureCreateView.as_view(), name='feature-create'),
    path('project/group/<int:pk>/features/add/', AddFeature, name='feature-add'),
    path('project/group/create/', FeatureGroupCreateView.as_view(), name='group-create'),
    path('project/group/<int:pk>/edit/', FeatureGroupDetailView.as_view(), name='group-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/features/<int:pk>/', FeatureDetailView.as_view(), name='feature-detail'),
    path('project/features/bugs/<int:pk>/', BugDetailView.as_view(), name="bug-detail"),
    path('project/sprints/create/', SprintCreateView.as_view(), name="sprint-create"),
    path('project/sprints/<int:pk>/', SprintDetailView.as_view(), name="sprint-detail"),
    path('project/sprints/<int:pk>/edit/', SprintEditView.as_view(), name="sprint-edit"),
]