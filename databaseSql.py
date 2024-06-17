import mysql.connector
from mysql.connector import Error
from main import download_playlist,download_video

hostname = "localhost"
username = "root"
password = ""
database = "ytdownloader"

def connection_db():
  try:
      # Connect to the MySQL server
      connection = mysql.connector.connect(
      host=hostname,
      user=username,
      password=password,
      database = database)
    
  except mysql.connector.Error as error:
      # Print an error message if connection fails
      print("Connection failed:", error)
      return
  return connection
   

def insert_into_playlist(yt_url:str):
    try:
      connection = connection_db()
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
    except Error as error:
       print(error)
    finally:
      connection.commit()
      print("Inserting to MySQL database successful!")
      connection.close()


def insert_video(yt_url:str):
    try:
      connection = connection_db()
      data = download_video(yt_url)
      mycommand = connection.cursor()
      mycommand.execute("INSERT INTO playlist(title, yt_url, yt_dw) VALUES(%s, %s, %s)",(data['titles'], data['urls'], yt_url))
    except Error as error:
       print(error)
    finally:
      connection.commit()
      connection.close()


def serach_for_video(yt_url:str):
    try:
        connection = connection_db()
        
        with connection.cursor() as mycommand:
            mycommand.execute("SELECT * FROM video WHERE yt_url = %s",(yt_url, ))
            data = mycommand.fetchall()
            if data is None:
               connection.close()
               return None
            return data
            
    except Error as error:
       print(error)


def serach_for_playlist(yt_url:str):
    try:
        connection = connection_db()

        with connection.cursor() as mycommand:
            mycommand.execute("SELECT title FROM video WHERE id IN ( SELECT videoID FROM videotoplaylist WHERE videoId IN (SELECT id FROM playlist WHERE yt_url = %s ))",(yt_url, ))
            data = mycommand.fetchall()
            if data is None:
               connection.close()
               return None
            return data
            
    except Error as error:
       print(error)


   

#print(serach_for_playlist("https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd"))


