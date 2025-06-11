# 🎵 Billboard Hot 100 Playlist Creator
This Python script automates playlist creation on Spotify, fetching the [Billboard Hot 100 songs](https://www.billboard.com/charts/hot-100/) from a given date using web scraping and API integration.


# ✨ Features
Web Scraping: Extracts song titles from Billboard's website using requests and BeautifulSoup.

Spotify API Integration: Authenticates using OAuth and creates a private playlist.

Automated Song Search: Searches for Billboard songs on Spotify based on their release year.

Error Handling: Skips songs that aren't found on Spotify, ensuring a smooth playlist creation process.

# 🔧 Prerequisites
Python 3.x

requests, beautifulsoup4, spotipy libraries

A Spotify Developer Account with API credentials (CLIENT_ID, CLIENT_SECRET).

# 🚀 Setup & Usage
- Clone the repository:

-> git clone https://github.com/yourusername/billboard-spotify-playlist.git

-> cd billboard-spotify-playlist

 - Set up environment variables for Spotify API authentication:

-> export CLIENT_ID="your_client_id"

-> export CLIENT_SECRET="your_client_secret"

-> Enter a date (YYYY-MM-DD), and the playlist will be created automatically in your Spotify account.

# 📌 Notes

Ensure your Spotify Developer Account is configured to allow playlist modifications.

Modify the user authentication section to match your Spotify username.

If some songs are missing, it means Spotify's library does not contain an exact match.

You can refer [Spotipy Documentation](https://spotipy.readthedocs.io/en/2.25.1/) to configure [Spotify Developer Account](https://developer.spotify.com/).


