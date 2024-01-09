from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)
