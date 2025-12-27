import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    AYRSHARE_API_KEY = os.getenv("AYRSHARE_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hackathon.db")
    CREDITS_FOR_UPLOAD = 5
    CREDITS_FOR_SOCIAL_POST = 5
