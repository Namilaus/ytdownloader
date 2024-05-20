import yt_dlp
# URL of the YouTube playlist

def download_playlist_specific(playlist_url:str)->list:


    # Options for downloading the playlist
    ydl_opts = {
        'format': 'best',
        'outtmpl': r'C:\Users\Schueler\Desktop\private\series\qhave_talkh_2\%(playlist_index)s_%(title)s.%(ext)s',  # Output template
        'yes-playlist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        playlist_dwurl = ydl.extract_info(playlist_url, download=False)
        
        return playlist_dwurl


arrayoflist = download_playlist_specific('https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd')

print(arrayoflist['entries'][0]['url'])

for index,info in enumerate(arrayoflist):
    print(info[18])
