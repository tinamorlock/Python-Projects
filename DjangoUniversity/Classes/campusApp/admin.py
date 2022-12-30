from django.contrib import admin
from .models import UniversityCampus

# registering UniversityCampus model
# note: has to be within app's directory

admin.site.register(UniversityCampus)
