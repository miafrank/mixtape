import factory
from mixtape.models.album import Album
from mixtape.tests.factories.artist_factory import ArtistFactory


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    name = "White Pony"
    spotify_link = "https://open.spotify.com/album/5LEXck3kfixFaA3CqVE7bC"
    total_tracks = "12"
    artists = factory.SubFactory(ArtistFactory)
