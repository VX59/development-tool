from django.contrib import admin
from .models import (Project, 
                    Feature, 
                    FeatureGroup,
                    Bug,
                    Sprint,)

admin.site.register(Project)
admin.site.register(Feature)
admin.site.register(FeatureGroup)
admin.site.register(Bug)
admin.site.register(Sprint)