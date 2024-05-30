from flask import Flask,request
from main import download_video,download_playlist,download_playlist_specific
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/<download_method>",methods=['GET','POST'])
def give_data(download_method:str):
    
    if download_method == "download_video":
        data = request.json
        dw_url = download_video(data['url'])
        
        return {
                'title':dw_url['titles'],
                'url': dw_url['urls']

                }

    elif download_method == "download_playlist":
        data = request.json
        dw_url = download_playlist(data['url'])

        return{
                'titles':dw_url['titles'],
                'url':dw_url['urls']
                }

    elif download_method == "download_playlist_specific":
        data = request.json
        dw_url = download_playlist_specific(data['url'], data['playliststart'])
        
        return{
                'titles':dw_url['titles'],
                'url':dw_url['urls']
                }


    return "bing chiling"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
