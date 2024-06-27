# YouTube Downloader

YouTube Downloader is a web application that allows users to download videos and playlists from YouTube. This application provides an easy-to-use interface to fetch video details and download links using the `yt_dlp` library.

## Features

- **Download Single Video**: Download a single video by providing its URL.
- **Download Playlist**: Download all videos in a playlist by providing the playlist URL.
- **Download Playlist From Specific Index**: Download videos from a specific starting point in a playlist.

## Technologies Used

- **Backend**: Python, Flask, `yt_dlp`, MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Other**: Flask-CORS for handling Cross-Origin Resource Sharing (CORS)

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- Flask
- `yt_dlp` library

### Clone the Repository

```bash
git clone https://github.com/yourusername/ytdownloader.git
cd ytdownloader

Set Up the Virtual Environment
bash
Code kopieren
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
Code kopieren
pip install -r requirements.txt
Configure Database
Ensure you have a MySQL database set up and update the databaseSql.py file with your database credentials.

python
Code kopieren
self.hostname = "localhost"
self.username = "root"
self.password = ""
self.database = "ytdownloader"
Run the Application
bash
Code kopieren
python server.py
The application will be accessible at https://localhost:8443.

Usage
Open the application in your web browser.
Enter the YouTube URL in the input field.
Select the desired download option (video, playlist, or playlist from a specific index).
Click the "Download" button to fetch the download link(s).
API Endpoints
Download Video
Endpoint: /download_video
Method: POST
Payload:
json
Code kopieren
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
Response:
json
Code kopieren
{
  "title": "Video Title",
  "url": "Download URL"
}
Download Playlist
Endpoint: /download_playlist
Method: POST
Payload:
json
Code kopieren
{
  "url": "https://www.youtube.com/playlist?list=PLAYLIST_ID"
}
Response:
json
Code kopieren
{
  "titles": ["Title 1", "Title 2", "..."],
  "urls": ["URL 1", "URL 2", "..."]
}
Download Playlist From Specific Index
Endpoint: /download_playlist_specific
Method: POST
Payload:
json
Code kopieren
{
  "url": "https://www.youtube.com/playlist?list=PLAYLIST_ID",
  "startIndex": 2
}
Response:
json
Code kopieren
{
  "titles": ["Title 2", "Title 3", "..."],
  "urls": ["URL 2", "URL 3", "..."]
}
Database Schema
Table video:

id (INT): Primary key
title (VARCHAR): Title of the video
yt_url (VARCHAR): URL of the video
yt_dw (VARCHAR): Download URL of the video
Table playlist:

id (INT): Primary key
yt_url (VARCHAR): URL of the playlist
length (INT): Number of videos in the playlist
Table videotoplaylist:

videoID (INT): Foreign key referencing video.id
playlistID (INT): Foreign key referencing playlist.id
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

License
This project is licensed under the MIT License.

Acknowledgements
yt-dlp for providing an excellent library to download YouTube videos.
Flask for making web development easy and straightforward.
