from config import Config

def post_to_social_media(caption: str, image_url: str, platforms: list):
    """Placeholder - will work once social-post-api is installed"""
    print(f"Would post: {caption}")
    print(f"To platforms: {platforms}")
    return {"status": "success", "message": "Package not installed yet"}

def get_post_status(post_id: str):
    return {"status": "pending"}

def get_supported_platforms():
    return ["twitter", "facebook", "instagram", "linkedin", "youtube", "reddit"]

