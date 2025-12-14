from .Group import Group

class GroupInvite:
    def __init__(self, code, groupId, clientrequests):
        self.clientrequests = clientrequests
        self.code = code
        self.groupId = groupId

        res = self.clientrequests.get(f"/groups/{self.groupId}")
        res = res.json()

        self.Group = Group(data=res, clientrequests=clientrequests)


    def join(self):
        res = self.clientrequests.post(f"/groups/{self.groupId}/request_to_join", {"auto_join_secret": self.code})
        # print(res.json())