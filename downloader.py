from io import BytesIO
from PIL import Image
from pytube import Playlist #pytube2
import os
import requests
import music_tag


playlist = Playlist("https://www.youtube.com/playlist?list=PLYHI_9Wc3IgkzmYCufwGBiHh2lSOBcSPR")

download_folder = "./downloads"

for video in playlist.videos:
    thumbnail = video.thumbnail_url
    title = video.title
    artist = video.author
    file = f"{download_folder}/{title}.mp3"
    
    if not os.path.isfile(file):
        response = requests.get(thumbnail)
        image = Image.open(BytesIO(response.content))
        image.convert('RGB').save(f"{download_folder}/thumbnail.jpeg", 'JPEG')
        video.streams.get_audio_only().download(output_path=download_folder, filename=f"{title}.mp3")
        tagging = music_tag.load_file(file)
        tagging["artist"] = artist
        
        with open(f"{download_folder}/thumbnail.jpeg", "rb") as img: 
            tagging["artwork"] = img.read()
        tagging.save()