import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from pprint import pprint

# https://developer.spotify.com/dashboard
CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
USER_ID = YOUR_USER_ID

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/"
full_url = f"{url}{date}"
print(full_url)

response = requests.get(full_url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_song_titles = [title.getText() for title in soup.find_all(
    name="span",
    class_="chart-element__information__song text--truncate color--primary")
]
# print(len(all_song_titles))
print(all_song_titles)

client_credentials_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="user-library-read playlist-modify-public"
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Creating the playlist
sp.user_playlist_create(user=USER_ID, name=f"Top 100 Songs Of {date}", public=True, description=f"This is a playlist with the top 100 songs from {date}.")

# Grabbing the id of the newly created playlist (new playlists are at index 0)
first_playlist_id = sp.current_user_playlists()["items"][0]["id"]
print(first_playlist_id)

# Searching all songs for ID's
song_id_list = []
for song in all_song_titles:
    try:
        song_id_list.append(sp.search(q=song, limit=1)["tracks"]["items"][0]["href"].split("tracks/")[1])
    except IndexError:
        continue
# Adding songs to the new playlist
sp.user_playlist_add_tracks(user=USER_ID, playlist_id=first_playlist_id, tracks=song_id_list)
