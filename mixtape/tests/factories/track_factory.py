import factory
from mixtape.models.track import Track
from mixtape.tests.factories.album_factory import AlbumFactory
from mixtape.tests.factories.artist_factory import ArtistFactory


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Track

    name = "Knife Party"
    artists = factory.SubFactory(ArtistFactory)
    album = factory.SubFactory(AlbumFactory)
