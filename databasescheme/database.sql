CREATE DATABASE IF NOT EXISTS ytdownloader;

USE ytdownloader;

CREATE TABLE IF NOT EXISTS video(
	id INT PRIMAY KEY,
	title VARCHAR(255)
);
