from django.contrib import admin
from .models import Problem

admin.register(Problem)(admin.ModelAdmin)
