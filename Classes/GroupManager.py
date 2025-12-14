from Classes.GroupInvite import GroupInvite
from Classes.Group import Group
class GroupManager:
    def __init__(self, clientrequests):
        self.clientrequests = clientrequests
    
    def fetchGroupInvite(self, code, groupId):
        return GroupInvite(code=code, clientrequests=self.clientrequests, groupId=groupId)
    
    def fetchGroup(self, groupId):
        res = self.clientrequests.get(f"/groups/{groupId}")
        res = res.json()

        self.Group = Group(data=res, clientrequests=self.clientrequests)