from Classes.UserProfileImage import *

class User:
    def __init__(self, clientrequests, data):
        self.clientrequests = clientrequests
        self.id = data.get("id")
        self.username = data.get("username")
        self.first_name = data.get("first_name")
        self.grade_display = data.get("grade_display")
        self.profile_image_url = data.get("profile_image_url")
        self.highlighted_achievement = data.get("highlighted_achievement")
        self.package_name = data.get("package_name")
        self.tutor = data.get("tutor")
        self.employee = data.get("employee")
        
        profile_image = data.get("profile_image", {})
        self.profile_image = UserProfileImage({
            "image_url": profile_image.get("image_url"),
            "profile_color": profile_image.get("profile_color"),
            "profile_letter": profile_image.get("profile_letter")
        })