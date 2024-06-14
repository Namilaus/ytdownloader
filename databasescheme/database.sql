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
