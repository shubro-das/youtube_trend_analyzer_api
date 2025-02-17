import json
from database.db_config import connect_db
from api_requests.fetch_trending import fetch_trending_videos

# Function to insert data into MySQL
def store_trending_videos():
    data = fetch_trending_videos()

    if not data:
        print("No data fetched!")
        return

    conn = connect_db()
    if not conn:
        print("Database connection failed!")
        return

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO trending_videos (video_id, title, channel, category, views, likes, comments, published_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
    views = VALUES(views), likes = VALUES(likes), comments = VALUES(comments), category = VALUES(category);
    """

    for video in data["items"]:
        video_id = video["id"]
        title = video["snippet"]["title"]
        channel = video["snippet"]["channelTitle"]
        category = video.get("category_name", "Unknown")
        views = video["statistics"].get("viewCount", 0)
        likes = video["statistics"].get("likeCount", 0)
        comments = video["statistics"].get("commentCount", 0)
        published_at = video["snippet"]["publishedAt"]

        cursor.execute(insert_query, (video_id, title, channel, category, views, likes, comments, published_at))

    conn.commit()
    cursor.close()
    conn.close()
    print("Trending videos stored successfully with categories!")

# Run the function
if __name__ == "__main__":
    store_trending_videos()







# import json
# import mysql.connector
# from database.db_config import connect_db
# from api_requests.fetch_trending import fetch_trending_videos

# # Function to insert data into MySQL
# def store_trending_videos():
#     data = fetch_trending_videos()

#     if not data:
#         print("No data fetched!")
#         return

#     conn = connect_db()
#     if not conn:
#         print("Database connection failed!")
#         return

#     cursor = conn.cursor()

#     insert_query = """
#     INSERT INTO trending_videos (video_id, title, channel, category, views, likes, comments, published_at)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#     ON DUPLICATE KEY UPDATE 
#     views = VALUES(views), likes = VALUES(likes), comments = VALUES(comments);
#     """

#     for video in data["items"]:
#         video_id = video["id"]
#         title = video["snippet"]["title"]
#         channel = video["snippet"]["channelTitle"]
#         category = video.get("category_name", "Unknown")  # Get category info from fetch_trending.py
#         views = video["statistics"].get("viewCount", 0)
#         likes = video["statistics"].get("likeCount", 0)
#         comments = video["statistics"].get("commentCount", 0)
#         published_at = video["snippet"]["publishedAt"]

#         cursor.execute(insert_query, (video_id, title, channel, category, views, likes, comments, published_at))

#     conn.commit()
#     cursor.close()
#     conn.close()
#     print("Trending videos stored successfully!")

# # Run the function
# if __name__ == "__main__":
#     store_trending_videos()
