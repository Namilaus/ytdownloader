import mysql.connector
from mysql.connector import Error


class database:

    def __init__(
        self, hostname: str, username: str, password: str, database: str
    ) -> None:

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
                database=self.database,
                port=13497,
            )

            # print(connection)

        except mysql.connector.Error as error:
            # Print an error message if connection fails
            print("Connection failed:", error)
            return None
        return connection

    def insert_into_playlist(self, yt_url: str, data: dict) -> int:
        try:
            connection = self.connection_db()
            if connection == None:
                return None
            # for element in range(0,data['playlist_length']):
            # print(data['titles'][element],data['urls'][element])
            mycommand = connection.cursor()
            mycommand.execute(
                "INSERT INTO playlist(yt_url, length) VALUES(%s,%s)",
                (yt_url, data["playlist_length"]),
            )
            mycommand.execute("SELECT id FROM playlist ORDER BY id DESC LIMIT 1")
            playlistID = mycommand.fetchone()  # get playlistId for the sql realiton

            for element in range(
                0, data["playlist_length"]
            ):  # inserting all of the playlist video into video sql table
                mycommand.execute(
                    "INSERT INTO video (title, yt_dw) VALUES (%s, %s)",
                    (data["titles"][element], data["urls"][element]),
                )
                mycommand.execute("SELECT id FROM video ORDER BY id DESC LIMIT 1")
                videoID = mycommand.fetchone()
                mycommand.execute(
                    "INSERT INTO videotoplaylist (videoID,playlistID) VALUES (%s, %s)",
                    (videoID[0], playlistID[0]),
                )
        except Error as error:

            print(error)
            return 405

        finally:

            connection.commit()
            connection.close()
            return 200

    def insert_video(self, yt_url: str, data) -> int:
        try:
            connection = self.connection_db()
            if connection == None:
                return None
            mycommand = connection.cursor()
            mycommand.execute(
                "INSERT INTO video(title, yt_url, yt_dw) VALUES(%s, %s, %s)",
                (data["titles"], yt_url, data["urls"]),
            )
        except Error as error:
            print(error)
            return 505
        finally:
            connection.commit()
            connection.close()
            return 200

    def serach_for_video(self, yt_url: str) -> list:
        try:
            connection = self.connection_db()
            if connection == None:
                return None

            with connection.cursor() as mycommand:
                mycommand.execute("SELECT * FROM video WHERE yt_url = %s", (yt_url,))
                data = mycommand.fetchall()
                if data is None:
                    return None

            connection.close()
            return data

        except Error as error:
            print(error)

    def serach_for_playlist(self, yt_url: str) -> list:
        try:
            connection = self.connection_db()
            if connection == None:
                return None
            with connection.cursor() as mycommand:  # instead of JOINs using WHERE because of speed and performance
                mycommand.execute(
                    "SELECT * FROM video WHERE id IN ( SELECT videoID FROM videotoplaylist WHERE playlistID IN (SELECT id FROM playlist WHERE yt_url = %s ))",
                    (yt_url,),
                )
                data = mycommand.fetchall()
                if data is None:
                    return None

            connection.close()
            return data

        except Error as error:
            print(error)


# print(serach_for_playlist("https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd"))
