import factory
from mixtape.models.artist import Artist


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist
        django_get_or_create = ('name', 'album_id', 'track_id',)

    name = "Deftones"
    # TODO: Update to model instances
    album_id = '123'
    track_id = '567'
