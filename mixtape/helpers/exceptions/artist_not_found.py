from mixtape.helpers.exceptions.base_api_exception import BaseAPIException


class ArtistNotFound(BaseAPIException):
    def message(self, artist):
        return f"Artist: {artist} not found"
