import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

#----------------------------------- Scraping the  Billboard Hot 100 --------------------------------------------------#

base_url = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
              " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
          }
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
endpoint= f"{base_url}{date}"
response = requests.get(endpoint, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
chart_data =soup.find(name="div", class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")


# song_artist = chart_data.select(selector="li span")
song_data = chart_data.find_all(name="li", class_="lrv-u-width-100p")
track_info = []
for song in song_data:
    if song.find(name="h3") is not None:

            track_dict = {"track": song.find(name="h3").text.strip(),
                          "artist": song.find(name="span").text.strip()}
            track_info.append(track_dict)









#------------------------------------------- Authentication with Spotify ----------------------------------------------#

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://example.com"
SCOPE = "playlist-modify-private"
CACHE_PATH = ".cache"

auth_manager = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=CACHE_PATH
)

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

# -------------------------------- Get User & Create Playlist -------------------------------- #

user_id = sp.current_user()["id"]

def create_playlist(name: str, public=False, description="Generated via Python script"):
    """Creates a new playlist and returns its ID."""
    playlist = sp.user_playlist_create(user=user_id, name=name, public=public, description=description)
    print(f"✅ Playlist '{name}' created.")
    return playlist["id"]

#-------------------------------------- Search Spotify for Songs ------------------------------------------------------#
MAX_TRACKS = 100

year = date.split("-")[0]

song_uris = []
for track in track_info:

    if "Featuring" in track["artist"]:
        cleaned_artist = track["artist"].split("Featuring")[0].strip()
    elif "With" in track["artist"]:
       cleaned_artist = track["artist"].split("With")[0].strip()
    else:
        cleaned_artist= track["artist"]
    print(cleaned_artist)
    query = f"track:{track['track']} artist:{cleaned_artist}"

    result =sp.search(q=query, type="track")

    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{track} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Billboard 100"

playlist_id = create_playlist(playlist_name)
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris[:MAX_TRACKS]                                                                                                                                                  )

# for song in song_names:
#     query = f"track:{song} year:{year}"
#
#     track =sp.search(q=query, limit=1, offset=0, type="track")
#     pprint(track)
#
