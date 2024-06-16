from pytube import Playlist
import pytube as yt

playlist = Playlist("https://www.youtube.com/playlist?list=PLYHI_9Wc3IgkzmYCufwGBiHh2lSOBcSPR")

download_folder = "./downloads"

for video in playlist.videos:
    title = video.title
    video.streams.filter(only_audio=True).first().download(output_path=download_folder, filename=title)