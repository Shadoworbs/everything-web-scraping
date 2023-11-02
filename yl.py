# import the necessary modules
import os
import yt_dlp
from datetime import datetime


# creating a folder for the videos
if os.path.isdir('videos') == True:
     os.chdir('videos')
else:
     os.mkdir('videos')
     os.chdir('videos')


cwd = os.getcwd()  # retrieves the current directory


# asks for video url to be downloaded
url = input('Enter a youtube, tiktok or instagram video link: ')

# Use default options for download (you will get the best video available)
opts = {}

# Start the download with the yt_dlp engine
with yt_dlp.YoutubeDL(opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    video_title = info_dict.get('title', None)


# Print success message when download is done
print(f'\n\nDownload complete ✅\nVideo location 👉 : {cwd}\nVideo name: {video_title}\n')


# check and print the site the video was downloaded from
def source(url):
    site: str=url.lower()
    if 'instagram.com' in site:
         return 'Source: Instagram'
    elif 'youtube.com' or 'youtu.be' in site:
         return 'Source: Youtube'
    elif 'tiktok.com' in site:
         return 'Source: Tiktok'
    return 'Source: Other'
print(f'{source(url)} \n------------------------------------------')




# log all the links to a text file for debugging
with open('log.txt', 'a', encoding="utf-8") as f:
    line1: str = url
    line2: str = video_title
    date = datetime.now()
    date_time = date.strftime('%Y-%m-%d %H:%M:%S')
    f.write(f"Video Location: {cwd} \nVideo Name: {line2} \nVideo Link: {line1} \nDate & Time of download: {date_time} \n\n")




