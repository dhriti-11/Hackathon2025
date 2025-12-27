import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CLOUDINARY_CLOUD_NAME = os.getenv("dz5jo04ya")
    CLOUDINARY_API_KEY = os.getenv("922452571857995")
    CLOUDINARY_API_SECRET = os.getenv("cHU_jzK1Yz9gB4d5N4sbUcjnNXw")
    AYRSHARE_API_KEY = os.getenv("8F7F8022-98A148CA-9264BEF6-C3563CF0")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hackathon.db")
    CREDITS_FOR_UPLOAD = 5
    CREDITS_FOR_SOCIAL_POST = 5
