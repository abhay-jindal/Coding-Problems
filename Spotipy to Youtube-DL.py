import os
import re
import spotipy
from youtube_dl import YoutubeDL
from urllib import request
from spotipy.oauth2 import SpotifyClientCredentials
from argparse import ArgumentParser
import concurrent.futures as concur


# Argparser
parser = ArgumentParser(description="Download Spotify playlist the easy way")


class Spotify2Ytube:
    __CLIENT_ID = "2a2a7269210f4bff9c1f802fd106cdd4"
    __CLIENT_SECRET = "43f9b8608ff049c287083eeda3917d62"

    def __init__(self, URI):
        self.playlistURI = URI
        self.auth_manager = SpotifyClientCredentials(client_id=self.__CLIENT_ID, client_secret=self.__CLIENT_SECRET)
        self.spotify = spotipy.Spotify(auth_manager=self.auth_manager)

    @staticmethod
    def get_ydl_opts(path):
        return {
            "format": "bestaudio/best",
            "outtmpl": f"./{path}/%(title)s.flac",
            'addmetadata':True,
            'postprocessor_args': ['-metadata artist=Flags'],
            "postprocessors": [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'flac',
                    'preferredquality': '320',
                },
            ],
        }

    def getPlaylistDetails(self):
        try:
            playlistName = self.spotify.playlist(self.playlistURI)["name"]
            playlistTracks = self.spotify.playlist_items(self.playlistURI, offset=0, fields="items.track.name,items.track.artists.name")["items"]

            tracksData = []
            if len(playlistTracks) > 0:
                 for track in playlistTracks:
                    name = track["track"]["name"].replace(" ", "+")
                    artist = track["track"]["artists"][0]["name"].replace(" ", "+")
                    tracksData.append(f"{name}+{artist}".encode("utf8"))
        except Exception as e:
            return "Unable to fetch spotify playlist details. Error: {}".format(e)
        return {"plName": playlistName, "plTracks": tracksData}

    @staticmethod
    def create_download_directory(dir_name):
        path = f"./{dir_name}"
        if os.path.exists(path):
            return path
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the download directory failed!")


    def download_tracks(self):
        playlist_details = self.getPlaylistDetails()
        if playlist_details.get("plName"):
            playlist_path = self.create_download_directory(playlist_details.get("plName"))

            with YoutubeDL(self.get_ydl_opts(playlist_path)) as ydl:
                tracks = playlist_details["plTracks"]
                numThreads = min(len(tracks), 10)
                executor = concur.ThreadPoolExecutor(numThreads)
                futures = [executor.submit(self.download, track, ydl) for track in tracks]
 
    @staticmethod
    def download(track, ydl):
        html = request.urlopen(f"https://www.youtube.com/results?search_query={track}")
        video_id = re.search(r"watch\?v=(\S{11})", html.read().decode()).group(1)
        if video_id:
            url = "https://www.youtube.com/watch?v=" + video_id
            try:
                ydl.download([url])
            except Exception:
                pass

if __name__ == "__main__":
    parser.add_argument("playlist_uri", metavar="PL_URI", type=str, help="Spotify playlist URI to download songs from")
    args = parser.parse_args()
    if args.playlist_uri:
        spotifyObj = Spotify2Ytube(args.playlist_uri)
        spotifyObj.download_tracks()
    else:
        print("Please provide a valid playlist uri to download.")
 




    