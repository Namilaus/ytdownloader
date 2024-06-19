import mysql.connector
from mysql.connector import Error
from main import download_playlist,download_video

class database:

    def __init__(self, hostname:str, username:str, password:str, database:str)->None:

        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database

    def connection_db(self):
        try:
            # Connect to the MySQL server
            connection = mysql.connector.connect(
            host=self.hostname,
            user=self.username,
            password=self.password,
            database = self.database)
    
        except mysql.connector.Error as error:
            # Print an error message if connection fails
            print("Connection failed:", error)
        return
    return connection
   

    def insert_into_playlist(self, yt_url:str, data):
        try:
            connection = self.connection_db()
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


    def insert_video(self, yt_url:str, data):
        try:
            connection = self.connection_db()
            mycommand = connection.cursor()
            mycommand.execute("INSERT INTO playlist(title, yt_url, yt_dw) VALUES(%s, %s, %s)",(data['titles'], data['urls'], yt_url))
        except Error as error:
            print(error)
        finally:
            connection.commit()
            connection.close()


    def serach_for_video(self, yt_url:str):
        try:
            connection = self.connection_db()
        
            with connection.cursor() as mycommand:
                mycommand.execute("SELECT * FROM video WHERE yt_url = %s",(yt_url, ))
                data = mycommand.fetchall()
                if data is None:
                    return None

            connection.close()
            return data
            
        except Error as error:
            print(error)


    def serach_for_playlist(self, yt_url:str):
        try:
            connection = self.connection_db()

            with connection.cursor() as mycommand:
                mycommand.execute("SELECT title FROM video WHERE id IN ( SELECT videoID FROM videotoplaylist WHERE videoId IN (SELECT id FROM playlist WHERE yt_url = %s ))",(yt_url, ))
                data = mycommand.fetchall()
                if data is None:
                    return None

            connection.close()
            return data
            
        except Error as error:
            print(error)


   

#print(serach_for_playlist("https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd"))


