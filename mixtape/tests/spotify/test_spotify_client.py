from unittest import TestCase
from mixtape.tests.factories.album_factory import AlbumFactory
from mixtape.tests.factories.artist_factory import ArtistFactory
from mixtape.tests.factories.track_factory import TrackFactory
from mixtape.models.track import Track
from mixtape.models.album import Album
from mixtape.models.artist import Artist

mixtape_data = {}


class TestSpotifyClient(TestCase):
    def setUp(self):
        spotify_link = "https://some_link.com"

        album_id = '123'
        track_id = '456'
        album_artists = ArtistFactory.create(
            album_id=album_id, track_id=track_id)
        album = AlbumFactory.create(
            id=album_id, spotify_link=spotify_link, artists=album_artists)

        track = TrackFactory.create(
            album=album, id=track_id, artists=album_artists)

        mixtape_data["artists"] = album_artists
        mixtape_data["album"] = album
        mixtape_data["track"] = track

    def tearDown(self):
        Artist.objects.all().delete()
        Album.objects.all().delete()
        Track.objects.all().delete()

    def successful_artist_top_tracks_response(self):
        result = {
            "top_tracks": [
                {
                    "artist_name": mixtape_data["artists"].name,
                    "track_name": mixtape_data["track"].name,
                    "album_name": mixtape_data["album"].name,
                    "spotify_link": mixtape_data["album"].spotify_link
                }
            ]
        }
        return result
