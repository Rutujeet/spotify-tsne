import requests

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_user_tracks(self):
        url = 'https://api.spotify.com/v1/me/tracks'
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()['items']

    def get_audio_features(self, tracks):
        track_ids = [track['track']['id'] for track in tracks]
        url = f'https://api.spotify.com/v1/audio-features?ids={",".join(track_ids)}'
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()['audio_features']