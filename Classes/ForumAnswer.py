from Classes.User import User
from Errors import InvalidActionError

class ForumAnswer:
    def like(self):
        if self.liked:
            raise InvalidActionError("This answer is already liked.")
        else:
            self.clientrequests.post(f"/qna/answers/{self.id}/votes", {})
            self.liked = True
    
    def unlike(self):
        if not self.liked:
            raise InvalidActionError("This answer is not liked.")
        else:
            self.clientrequests.post(f"/qna/answers/{self.id}/votes", {})
            self.liked = False

    def __init__(self, clientrequests, data):
        if "results" in data.keys():
            data = data['results']
        
        # Properties
        self.id = data.get("id")
        self.content = data.get("body")
        self.author = User(clientrequests, data.get("user"))
        self.votes = data.get("qna_votes_count")
        self.correct = data.get("correct")
        self.questionId = data.get("question_id")

        self.clientrequests = clientrequests
        self.liked = False
