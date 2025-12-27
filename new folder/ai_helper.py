import requests
from PIL import Image
from io import BytesIO
from google import genai
from storage import upload_image_to_cloud

url = upload_image_to_cloud("waste.png")

def analyze_image(image_url: str) -> dict:
    
    get_image = requests.get(image_url)
    data = get_image.content

    image = Image.open(BytesIO(data))

    client = genai.Client(api_key="AIzaSyD3rEaTidd1vO0TvD2uJbTxqWdjrSyK6Uo") ##can only be used for 20 times

    problem= client.models.generate_content(
    model="gemini-2.5-flash", contents=[image,"tell the problem seen in image in 2 words"])

    authority = client.models.generate_content(
    model="gemini-2.5-flash", contents=[image,"let a person live in india then respective to that in few words provide only the name of two authorities and  their contact number to solve this problem."])
    
    caption = client.models.generate_content(
    model="gemini-2.5-flash", contents=[image,"only prove the caption with hashtag without giving details so that i can post on social media"])

    return {
        "problem": problem.text,
        "authority" :authority.text,
        "caption" : caption.text
    }



###extract the url of image uploaded from cloudinary and put it in place of image_url

#to check
# a  = analyze_image("url") ##dummy image
# print("problem:\n")
# print(a['problem'])
# print("\n")
# print(a['authority'])
# print("caption\n")
# print(a['caption'])




# No need

# def get_authority_contacts(authority: str) -> dict:
#     """Get contact info for authority"""
#     contacts = {
#         "municipality": {"name": "Municipal Corporation", "phone": "123-456-7890"},
#         "PWD": {"name": "Public Works Department", "phone": "123-456-7891"},
#         "water_board": {"name": "Water Board", "phone": "123-456-7892"}
#     }
#     return contacts.get(authority, {})

# no need