from django.contrib import admin
from .models import UniversityClasses

# registering UniversityClasses
# note for future use: must be registered within app's directory

admin.site.register(UniversityClasses)
