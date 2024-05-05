import pytube
import yt_dlp as youtube_dl
import requests
import os 
import bs4
import json
from pytube.exceptions import AgeRestrictedError
import bs4 as BeautifulSoup

class Youtube_Downloader:
    def __init__(self) -> None:
        self.download_path = "./Voice_to_subtitles/src/Resources"

    def download_video(self):
        pl = pytube.Playlist("https://www.youtube.com/playlist?list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU")
        pl = pl.video_urls
        for i in pl:
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
            }],
             'outtmpl':self.download_path + '/%(title)s.%(ext)s',
               }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([i])


test= Youtube_Downloader()
test.download_video()
