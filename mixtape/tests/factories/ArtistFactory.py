import factory
from models.artist import Artist


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist
    name = "Deftones"
