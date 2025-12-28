from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from collections import Counter
from sklearn.linear_model import LogisticRegression

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
