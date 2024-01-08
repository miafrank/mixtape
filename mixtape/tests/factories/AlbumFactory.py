import factory
from mixtape.models.album import Album
from mixtape.models.artist import Artist


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    name = "White Pony"
    spotify_link = "https://open.spotify.com/album/5LEXck3kfixFaA3CqVE7bC"
    total_tracks = "12"
    artists = [Artist(name="Deftones")]
