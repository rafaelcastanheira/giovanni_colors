from django.shortcuts import render, get_object_or_404
from .models import Art
from .utils import split_by_columns

app_name = "portfolio"


def homepage(request):
    return render(request, 'portfolio/homepage.html')


def portfolio(request, art_type):
    if art_type in ("street",):
        arts = Art.objects.filter(art_type=Art.ArtType.STREET).order_by("-created_on")
    elif art_type in ("canvas",):
        arts = Art.objects.filter(art_type=Art.ArtType.CANVAS).order_by("-created_on")
    elif art_type in ("design",):
        arts = Art.objects.filter(art_type=Art.ArtType.DESIGN).order_by("-created_on")
    else:
        arts = Art.objects.all().order_by("-created_on")

    data = split_by_columns(arts)
    data["art_type"] = art_type

    return render(request, 'portfolio/portfolio.html', data)
