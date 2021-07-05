from django.shortcuts import render, get_object_or_404
from .models import Art
from .utils import split_by_rows

app_name = "portfolio"


def homepage(request, art_type="all"):
    if art_type in ("indoor",):
        arts = Art.objects.filter(art_type=Art.ArtType.INDOOR).order_by("-created_on")
    elif art_type in ("outdoor",):
        arts = Art.objects.filter(art_type=Art.ArtType.OUTDOOR).order_by("-created_on")
    else:
        arts = Art.objects.all().order_by("-created_on")

    data = split_by_rows(arts)
    data["art_type"] = art_type

    return render(request, 'portfolio/homepage.html', data)

