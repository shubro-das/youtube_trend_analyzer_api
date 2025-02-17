CREATE DATABASE IF NOT EXISTS youtube_trends;
USE youtube_trends;

CREATE TABLE IF NOT EXISTS trending_videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    video_id VARCHAR(50) UNIQUE,
    title VARCHAR(255),
    channel VARCHAR(255),
    category VARCHAR(100),
    views BIGINT,
    likes BIGINT,
    comments BIGINT,
    published_at DATETIME,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
