from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=50)
    spotify_link = models.CharField()
    total_tracks = models.IntegerField()
    artists = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="artist_album")
