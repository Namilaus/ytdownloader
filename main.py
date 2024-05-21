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


video_list_info = download_playlist_specific('https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd')

playlist_length = video_list_info['playlist_count']

for info in video_list_info:
    print(info)

for index in range(0,playlist_length):
    print(f'{index+1} link - {video_list_info["entries"][index]["url"]}')

