from django.db import models
from artist import Artist
from album import Album


class Track(models.Model):
    name = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
