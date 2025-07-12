import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()  # Optional if using .env

client_id = os.getenv("9d0b70f9e4794aa2b2baa4627e7a015e")
client_secret = os.getenv("746bdd1f21a442c7a0ec5ab39fab9d84")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

def recommend_music(genre):
    results = sp.search(q=f'genre:{genre}', type='track', limit=5)
    tracks = []
    for item in results['tracks']['items']:
        track_info = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'url': item['external_urls']['spotify']
        }
        tracks.append(track_info)
    return tracks
