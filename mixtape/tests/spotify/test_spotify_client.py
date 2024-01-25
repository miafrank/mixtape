from unittest import mock, TestCase
import pytest
from mixtape.helpers.exceptions.artist_not_found import ArtistNotFound
from mixtape.tests.factories.album_factory import AlbumFactory
from mixtape.tests.factories.artist_factory import ArtistFactory
from mixtape.tests.factories.track_factory import TrackFactory
from mixtape.models.track import Track
from mixtape.models.album import Album
from mixtape.models.artist import Artist
# from mixtape.client.spotify.spotify_client import SpotifyClient
import mixtape.client.spotify.spotify_client

mixtape_data = {}


class TestSpotifyClient(TestCase):
    def setUp(self):
        spotify_link = "https://some_link.com"
        album_id = '123'
        track_id = '456'

        artist = ArtistFactory.create(album_id=album_id, track_id=track_id)
        album = AlbumFactory.create(
            id=album_id, spotify_link=spotify_link, artists=artist)
        track = TrackFactory.create(album=album, id=track_id, artists=artist)

        mixtape_data["artists"] = artist
        mixtape_data["album"] = album
        mixtape_data["track"] = track

    def tearDown(self):
        Artist.objects.all().delete()
        Album.objects.all().delete()
        Track.objects.all().delete()

    # TODO: Move to /helpers
    def successful_artist_top_tracks_response(self):
        result = {
            "top_tracks": [
                {
                    "artist_name": mixtape_data["artists"].name,
                    # Update to 'tracks: [name, url, album name, album url]
                    "track_name": mixtape_data["track"].name,

                    # TODO: move to top albums by artist helper
                    "album_name": mixtape_data["album"].name,
                    # TODO: move to top albums by artist helper
                    "spotify_link": mixtape_data["album"].spotify_link
                }
            ]
        }
        return result

    @pytest.mark.django_db
    @mock.patch('mixtape.client.spotify.spotify_client')
    def test_successful_response_when_artist_not_found_in_search(
            self, mock_spotify_client):

        response = self.successful_artist_top_tracks_response()
        mock_spotify_client.search.return_value = response
        top_ten_tracks = mock_spotify_client.search('Deftones')
        assert top_ten_tracks == response

    @pytest.mark.django_db
    @mock.patch(
        'mixtape.client.spotify.spotify_client')
    def test_exception_raised_when_artist_not_found_in_search(
            self, mock_spotify_client):
        # response = {
        #     "error":  f"Artist {mixtape_data["artists"].name} not found"
        # }
        # mock_spotify_client.top_ten_tracks_by_artist.return_value = (
        #     ArtistNotFound(message="not found"))
        # # with pytest.raises(ArtistNotFound):
        # top_ten_tracks_error = mock_spotify_client.top_ten_tracks_by_artist(
        #     'Deftones')
        # assert top_ten_tracks_error == response
        mock_spotify_client.search.return_value = ArtistNotFound(
            message="Artist Deftones not found")
        with pytest.raises(ArtistNotFound, match="Artist Deftones not found"):
            mock_spotify_client.search('Deftones')
