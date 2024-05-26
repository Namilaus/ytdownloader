import yt_dlp

def download_video(video_url:str)->dict:

    # Options for downloading the playlist
    ydl_opts = {
            'format':'best',
            'forceurl':True
            }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the video
        video_info = ydl.extract_info(video_url, download=False)
        
    playlist_urls = {
                'titles':video_info['fulltitle'],
                'urls':video_info['url']
            }

    return playlist_urls

#print(download_video('https://www.youtube.com/watch?v=Jvzdd14oqMw'))

def download_playlist(playlist_url:str)->dict:


    ydl_opts = {
        'format': 'best',
        'yes-playlist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
    playlist_length = playlist_info['playlist_count']
    
    playlist_urls = {
                'titles':[],
                'urls':[]
            }

    for index in range(0,playlist_length):
        playlist_urls['titles'].append(playlist_info['entries'][index]['fulltitle'])
        playlist_urls['urls'].append(playlist_info['entries'][index]['url'])    
    
    return playlist_urls


#print(download_playlist('https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd'))

def download_playlist_specific(playlist_url:str,playliststart:int)->dict:
    ydl_opts = {
            'format':'best',
            'yes-playlist':True,
            'playliststart': str(playliststart)
            }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
    
    playlist_length = playlist_info['playlist_count'] - playliststart + 1
    print(playlist_length)
    playlist_urls = {
                'titles':[],
                'urls':[]
            }

    for index in range(0,playlist_length):
        playlist_urls['titles'].append(playlist_info['entries'][index]['fulltitle'])
        playlist_urls['urls'].append(playlist_info['entries'][index]['url'])    
    
    return playlist_urls



#print(download_playlist_specific('https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd',2))
