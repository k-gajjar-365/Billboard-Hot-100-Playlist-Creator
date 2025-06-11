import requests
from bs4 import BeautifulSoup
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? write date in (YYY-MM-DD) format : ")
print(date)
year = date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
HEADER = {
    "USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko)"
                 " Chrome/137.0.0.0 Safari/537.36"
}
response = requests.get(url=URL,headers=HEADER)

soup = BeautifulSoup(response.text,"html.parser")


song_list = [song.getText().strip() for song in soup.select("li ul li h3")]


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_TOKEN = os.environ.get("CLIENT_SECRET")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_TOKEN,
        show_dialog=True,
        cache_path="token.txt",
        username="Kirtan Gajjar",))

# Making Playlist
user_id = sp.current_user()["id"]
name = f"{date} Billboard top 100"
playlist = sp.user_playlist_create(user=user_id,
                                      name=name,
                                      public=False)

uri = []
for song in song_list:
    song_response = sp.search(q=f"year:{year} track:{song}",type="track")
    try:
        uri.append(song_response["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist["id"],uri)

