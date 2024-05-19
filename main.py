import yt_dlp
# URL of the YouTube playlist

def download_playlist_specific(playlist_url:string,start:int):


    # Options for downloading the playlist
    ydl_opts = {
        'format': 'best',
        'outtmpl': r'C:\Users\Schueler\Desktop\private\series\qhave_talkh_2\%(playlist_index)s_%(title)s.%(ext)s',  # Output template
        'yes-playlist': True,
        'playlist_items': '47-' # Indicates that the URL points to a playlist
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        ydl.extract_info(playlist_url, download=True)
