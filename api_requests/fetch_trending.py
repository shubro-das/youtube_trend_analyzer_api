import requests
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Fetch category details from YouTube API
def fetch_video_categories(region_code="US"):
    url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={region_code}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        categories = {item["id"]: item["snippet"]["title"] for item in response.json()["items"]}
        return categories
    else:
        print("Error fetching categories:", response.status_code)
        return {}

# Fetch trending videos and add category info
def fetch_trending_videos(region_code="BD", max_results=10):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={region_code}&maxResults={max_results}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        trending_data = response.json()
        categories = fetch_video_categories()  # Get category info
        for video in trending_data["items"]:
            video["category_name"] = categories.get(video["snippet"]["categoryId"], "Unknown")
        return trending_data
    else:
        print("Error fetching data:", response.status_code)
        return None

if __name__ == "__main__":
    data = fetch_trending_videos()
    print(data)  # Print response to check category info
















# import requests
# import os
# from dotenv import load_dotenv

# # Load API Key from .env
# load_dotenv()
# API_KEY = os.getenv("YOUTUBE_API_KEY")

# # Fetch trending videos in Bangladesh
# def fetch_trending_videos(region_code="BD", max_results=10):
#     url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={region_code}&maxResults={max_results}&key={API_KEY}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Error fetching data:", response.status_code)
#         return None

# if __name__ == "__main__":
#     data = fetch_trending_videos()
#     print(data)  # Print response to check the structure
