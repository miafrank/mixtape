from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=50)
    artists = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="artist_track")
    album = models.OneToOneField("Album", on_delete=models.CASCADE)
