class Group:
    def __init__(self, data, clientrequests):
        group = data.get("group", {})

        self.id = group.get("id")
        self.name = group.get("name")
        self.education_type = group.get("education_type", {})
        self.school_track = group.get("school_track", {})
        self.grade = group.get("grade", {})
        self.school = group.get("school")
        self.small_image = group.get("small_image")
        self.normal_image = group.get("normal_image")
        self.image_url = group.get("image_url")
        self.total_members = group.get("total_members")
        self.owned_group = group.get("owned_group")
        self.status = group.get("status")
        self.institute = group.get("institute")
        self.total_inactive_licenses = group.get("total_inactive_licenses")
        self.is_owner = group.get("is_owner")
        self.is_primary_owner = group.get("is_primary_owner")
        self.is_manager = group.get("is_manager")
        self.creator = group.get("creator", {})
        self.shared = group.get("shared")
        self.subject_data = group.get("subject_data", {})
        self.requested_to_join_count = group.get("requested_to_join_count")
        self.auto_join = group.get("auto_join")
        self.auto_join_secret = group.get("auto_join_secret")
        self.success = data.get("success")

        self.clientrequests = clientrequests
    
    def leave(self):
        self.clientrequests.delete(f"/group/{self.id}/leave_group")
        return True