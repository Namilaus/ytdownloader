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
```

### Set Up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```bash
pip install yt_dlp mysql-connector flask flask-cors
```
### Configure Database
Ensure you have a MySQL database set up and update the databaseSql.py file with your database credentials.

```python
self.hostname = "localhost"
self.username = "root"
self.password = ""
self.database = "ytdownloader"
```
### Run the Application
```bash
python server.py
```

The application will be accessible at https://localhost:8443.

### Usage
1. Open the application in your web browser.
2. Enter the YouTube URL in the input field.
3. Select the desired download option (video, playlist, or playlist from a specific index).
4. Click the "Download" button to fetch the download link(s).
### API Endpoints
## Download Video
- Endpoint: /download_video
- Method: POST
- Payload:
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}```
- Response:
```json
{
  "title": "Video Title",
  "url": "Download URL"
}```
## Download Playlist
- Endpoint: /download_playlist
- Method: POST
- Payload:
```json
{
  "url": "https://www.youtube.com/playlist?list=PLAYLIST_ID"
}```
- Response:
```json
{
  "titles": ["Title 1", "Title 2", "..."],
  "urls": ["URL 1", "URL 2", "..."]
}```
## Download Playlist From Specific Index
- Endpoint: /download_playlist_specific
- Method: POST
- Payload:
```json
{
  "url": "https://www.youtube.com/playlist?list=PLAYLIST_ID",
  "startIndex": 2
}```
- Response:
```json
{
  "titles": ["Title 2", "Title 3", "..."],
  "urls": ["URL 2", "URL 3", "..."]
}```
### Database Schema
```sql
-- create database
CREATE DATABASE IF NOT EXISTS ytdownloader;

-- use database to create tables
USE ytdownloader;

-- create tables
CREATE TABLE IF NOT EXISTS video(
	id INT PRIMARY KEY AUTO_INCREMENT,
	yt_url VARCHAR(128),
	yt_dw VARCHAR(1502) NOT NULL,
	title VARCHAR(255)	NOT NULL
);

CREATE TABLE IF NOT EXISTS playlist(
	id INT PRIMARY KEY AUTO_INCREMENT,
	yt_url VARCHAR(128) NOT NULL,
	length SMALLINT NOT NULL

);

CREATE TABLE IF NOT EXISTS videotoplaylist(
	videoID INT NOT NULL,
	playlistID INT NOT NULL
);

-- add foreign keys

ALTER TABLE videotoplaylist ADD FOREIGN KEY(videoID) REFERENCES video(id);
ALTER TABLE videotoplaylist ADD FOREIGN KEY(playlistID) REFERENCES playlist(id);
```
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

# License
This project is licensed under the MIT License.

# Acknowledgements
yt-dlp for providing an excellent library to download YouTube videos.
Flask for making web development easy and straightforward.
