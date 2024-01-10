import factory
from mixtape.models.artist import Artist


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist

    name = "Deftones"
    album_id = '123'
    track_id = '567'
