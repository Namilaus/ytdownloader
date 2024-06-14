import mysql.connector
from main import download_playlist,download_video

hostname = "localhost"
username = "root"
password = ""
database = "ytdownloader"

def insert_into_playlist(yt_url:str):
    try:
      # Connect to the MySQL server
      connection = mysql.connector.connect(
      host=hostname,
      user=username,
      password=password,
      database = database

      )
    except mysql.connector.Error as err:
        # Print an error message if connection fails
        print("Connection failed:", err)
        return
  
    data = download_playlist(yt_url)
    #for element in range(0,data['playlist_length']):
    #print(data['titles'][element],data['urls'][element])
    mycommand = connection.cursor()
    mycommand.execute("INSERT INTO playlist(yt_url, length) VALUES(%s,%s)",(yt_url,data['playlist_length']))
    mycommand.execute("SELECT id FROM playlist ORDER BY id DESC LIMIT 1")
    playlistID = mycommand.fetchone()
  

    for element in range(0,data['playlist_length']):
      mycommand.execute("INSERT INTO video (title, yt_dw) VALUES (%s, %s)",(data['titles'][element],data['urls'][element]))
      mycommand.execute("SELECT id FROM video ORDER BY id DESC LIMIT 1")
      videoID = mycommand.fetchone()
      mycommand.execute("INSERT INTO videotoplaylist (videoID,playlistID) VALUES (%s, %s)", (videoID[0],playlistID[0]))
    connection.commit()
    print("Connection to MySQL server successful!")

    connection.close()

def insert_video(yt_url:str):
    try:
      # Connect to the MySQL server
      connection = mysql.connector.connect(
      host=hostname,
      user=username,
      password=password,
      database = database

      )
    except mysql.connector.Error as err:
        # Print an error message if connection fails
        print("Connection failed:", err)
        return
    data = download_video(yt_url)
    mycommand = connection.cursor()
    mycommand.execute("INSERT INTO playlist(title, yt_url, yt_dw) VALUES(%s,%s, %s)",(data['titles'], data['urls'], yt_url))
    connection.commit()
    connection.close()



    

   

#insert_into_playlist("https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd")


