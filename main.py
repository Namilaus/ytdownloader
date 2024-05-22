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
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
    playlist_length = playlist_info['playlist_count']


    playlist_urls = list()

    for index in range(0,playlist_length):
        #print(f'{index+1} link - {video_list_info["entries"][index]["url"]}')
        playlist_urls.append(playlist_info['entries'][index]['url'])    
    
    return playlist_urls

print(download_playlist_specific('https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd'))

    
