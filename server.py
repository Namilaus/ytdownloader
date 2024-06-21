from flask import Flask,request
from main import download_video,download_playlist,download_playlist_specific
from flask_cors import CORS
from databaseSql import database

app = Flask(__name__)
CORS(app)
database = database("localhost", "root", "", "ytdownloader")

@app.route("/<download_method>",methods=['GET','POST'])
def give_data(download_method:str):
    # checking POST url
    if download_method == "download_video":
        try:
            data = request.json # searching for download url in database for faster respond
            result = database.serach_for_video(data['url'])
            if len(result) == 0 or result == None: # if its not in database then we scrap it and savte to database for future use
                dw_url = download_video(data['url'])
                database.insert_video(data['url'],dw_url)
                return {
                'title':dw_url['titles'],
                'url': dw_url['urls']

                }
            else:
                return {
                'title':result[0][3],
                'url': result[0][2]

                }
        except TypeError as err:
            print(err)
            return "error",505

    elif download_method == "download_playlist":
        try:
            data = request.json
            results = database.serach_for_playlist(data['url'])
            if len(results) == 0 or results == None:
                dw_url = download_playlist(data['url'])
                database.insert_into_playlist(data['url'], dw_url)

                return{
                    'titles':dw_url['titles'],
                    'urls':dw_url['urls']
                    }
            else:
                urls = list()  # prepare data to return
                titles = list()
                for index in range(0,len(results)):
                    urls.append(results[index][2])
                    titles.append(results[index][3])
                return{
                    'titles':titles,
                    'urls':urls
                    }
        except TypeError as err:
            print(err)
            return "error",505

    elif download_method == "download_playlist_specific":
        try:
            data = request.json
            dw_url = download_playlist_specific(data['url'], data['startIndex'])
        
            return{
                    'titles':dw_url['titles'],
                    'urls':dw_url['urls']
                }
        except TypeError as err:
            print(err)
            return "error",505


    return "bing chiling"


if __name__ == '__main__':
    # 8443 port because cloudflare resolve just few ports and 8443 is one of them
    
    app.run(ssl_context = 'adhoc',debug=True,host='0.0.0.0',port=8443)
