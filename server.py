from flask import Flask,request
from main import download_video,download_playlist,download_playlist_specific
from flask_cors import CORS
from databaseSql import database


app = Flask(__name__)
CORS(app)
database = database("localhost", "root", "", "ytdownloader")

@app.route("/<download_method>",methods=['GET','POST'])
def give_data(download_method:str):
    
    if download_method == "download_video":
        try:

            data = request.json
            result = database.serach_for_video(data['url'])
            if len(result) == 0 or result == None:
                dw_url = download_video(data['url'])
                database.insert_video(dw_url)
                return {
                'title':dw_url['titles'],
                'url': dw_url['urls']

                }
            else:
                return {
                'title':result[0][3],
                'url': result[0][2]

                }
        except:
            return "error",505

    elif download_method == "download_playlist":
        try:
            data = request.json
            dw_url = download_playlist(data['url'])

            return{
                    'titles':dw_url['titles'],
                    'urls':dw_url['urls']
                }
        except:
            return "error",505

    elif download_method == "download_playlist_specific":
        try:
            data = request.json
            dw_url = download_playlist_specific(data['url'], data['startIndex'])
        
            return{
                    'titles':dw_url['titles'],
                    'urls':dw_url['urls']
                }
        except:
            return "error",505


    return "bing chiling"


if __name__ == '__main__':
    # 8443 port because cloudflare resolve just few ports
    
    app.run(ssl_context = 'adhoc',debug=True,host='0.0.0.0',port=8443)
