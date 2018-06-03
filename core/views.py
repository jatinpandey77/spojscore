from django.shortcuts import render
from .models import Problem

def index(request):
    problems = Problem.objects.all()
    return render(request, 'core/core.html', {'problems': problems})
