from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from collections import Counter
#from sklearn.linear_model import LogisticRegression

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-read-recently-played"
    )
)

results = sp.current_user_recently_played(limit=50)
for i in results['items']:
    track = i['track']
    print(f"Played {track['name']} by {track['artists'][0]['name']}")

genres = []
for i in results['items']:
    # get id
    # get artist
    # get genre and put it into genres
    artist_id = i['track']['artists'][0]['id']
    artist = sp.artist(artist_id)
    artist_genres = artist['genres']
    genres.extend(artist_genres)
    print(f"Artist genres: {artist_genres}")

