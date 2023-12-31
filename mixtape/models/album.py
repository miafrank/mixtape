from django.db import models
from artist import Artist


class Album(models.Model):
    name = models.CharField(max_length=50)
    total_tracks = models.IntegerField(MinValueValidator=1)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
