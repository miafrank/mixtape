from unittest import mock, TestCase
from mixtape.models.album import Album
from mixtape.models.artist import Artist
from mixtape.models.track import Track
from mixtape.tests.factories import ArtistFactory, TrackFactory, AlbumFactory
from mixtape.client.spotify.spotify_client import SpotifyClient

# TODO WIP:
# Creating objects in setup but need to access across multiple
# In JS or Rails you can use let and assign value later
# What is the equal or replacement for that in py?
# How to create multiple factories at once factorybot?


class TestSpotifyClient(TestCase):
    def setUp(self):
        artist = ArtistFactory.create()
        album = AlbumFactory.create(artists=[artist])
        TrackFactory.create(album=album)

    def tearDown(self):
        Album.objects.all().delete()
        Track.objects.all().delete()
        Artist.objects.all().delete()

    def successful_artist_top_tracks_response():
        return {[]}

    @mock.patch('mixtape.client.spotify.spotify_client')
    def test_when_artist_found(mock_spotify_client):
        mock_spotify_client.artist_top_tracks.return_value = ""
