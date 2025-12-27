from config import Config
from storage import upload_image_to_cloud
from ai_helper import analyze_image

url = upload_image_to_cloud("waste.png")

# get the url of uploaded image in cloudinary and use it in analyze image("url")


# remove comment only for testing purpose
# a = analyze_image("url")
# b = a['caption']

import requests


def post_to_social_media(caption: str, image_url: str, platforms: list):

    """Placeholder - will work once social-post-api is installed"""
    print(f"Would post: {caption}")
    print(f"To platforms: {platforms}")
    return {"status": "success", "message": "Package not installed yet"}

def get_post_status(post_id: str):
    url1 = "https://api.ayrshare.com/api/post"
    headers = {
    "Authorization": "Bearer 8F7F8022-98A148CA-9264BEF6-C3563CF0",
    "Content-Type": "application/json"
    }
    data = {
    "post": "b",
    "platforms": get_supported_platforms(),
    "mediaUrls": ["url"]
    }

    response = requests.post(url1, json=data, headers=headers)
    print(response.json())

    return {"status": "posted"}

def get_supported_platforms():
    return ["twitter", "facebook", "instagram", "linkedin", "youtube", "reddit"]
