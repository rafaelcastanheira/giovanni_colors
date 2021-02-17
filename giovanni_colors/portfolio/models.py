from django.db import models
from django.db.models import IntegerChoices


class Art(models.Model):
    class ArtType(IntegerChoices):
        STREET = 1
        CANVAS = 2
        DESIGN = 3

    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    art_type = models.IntegerField(choices=ArtType.choices, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/images/')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
