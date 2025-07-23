from Classes.GroupInvite import GroupInvite

class GroupManager:
    def __init__(self, clientrequests):
        self.clientrequests = clientrequests
    
    def fetchGroupInvite(self, code, groupId):
        return GroupInvite(code=code, clientrequests=self.clientrequests, groupId=groupId)