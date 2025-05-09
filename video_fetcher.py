import requests
import random
import os
from config import PEXELS_API_KEY

def fetch_background_video(keyword, save_dir="temp"):
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    response = requests.get(f"https://api.pexels.com/videos/search?query={keyword}&per_page=5", headers=headers)
    data = response.json()
    videos = data.get("videos", [])
    if not videos:
        return None

    video_url = random.choice(videos)["video_files"][0]["link"]
    filename = os.path.join(save_dir, f"{keyword}_background.mp4")

    video_data = requests.get(video_url).content
    with open(filename, "wb") as f:
        f.write(video_data)

    return filename
