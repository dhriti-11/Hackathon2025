
def analyze_image(image_url: str) -> dict:
    """
    Analyze civic issue image and return category, authority, caption.
    
    TODO: AI teammate - replace this with real AI API call
    """
    # fake data for testing
    # replace the below with whatever is needed
    return {
        "category": "problem",
        "authority": "PWD",
        "caption": " Problem spotted! Needs urgent repair. @CityPWD #FixOurRoads"
    }


def get_authority_contacts(authority: str) -> dict:
    """Get contact info for authority"""
    contacts = {
        "municipality": {"name": "Municipal Corporation", "phone": "123-456-7890"},
        "PWD": {"name": "Public Works Department", "phone": "123-456-7891"},
        "water_board": {"name": "Water Board", "phone": "123-456-7892"}
    }
    return contacts.get(authority, {})

