import factory
from mixtape.models.artist import Artist
from mixtape.models.track import Track
from mixtape.tests.factories.ArtistFactory import ArtistFactory


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Track
    name = "Knife Party"
    artists = [Artist(name="Deftones")]
    album = ArtistFactory(name="White Pony")
