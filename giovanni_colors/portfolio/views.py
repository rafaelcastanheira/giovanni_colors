from django.shortcuts import render
from .models import Art
from .utils import split_by_columns

app_name = "portfolio"


def homepage(request):
    return render(request, 'portfolio/homepage.html')


def portfolio(request):
    arts = Art.objects.all().order_by("-created_on")
    return render(request, 'portfolio/portfolio.html', split_by_columns(arts))
