from django.shortcuts import render
from .models import Art


def home(request):
    arts = Art.objects.all()
    return render(request, 'portfolio/home.html', {'arts': arts})