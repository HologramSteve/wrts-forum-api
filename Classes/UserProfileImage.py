class UserProfileImage:
    def __init__(self, data):
        self.image_url = data.get("image_url")
        self.profile_color = data.get("profile_color")
        self.profile_letter = data.get("profile_letter")