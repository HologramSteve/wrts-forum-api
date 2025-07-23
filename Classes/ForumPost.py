from Classes.User import User
from Classes.ForumAnswer import ForumAnswer

class ForumPost:
    def __init__(self, data: dict, clientrequests):
        self.clientrequests = clientrequests
        
        # if "results" in data.keys():
        #     data = data['results']

        # Properties
        data = data['qna_question']
        self.id = data['id']
        self.title = data['title']
        self.content = data['contents']
        self.topic = data.get("topic")
        self.closed = data.get("closed")
        self.author = User(clientrequests, data['user'])
        self.answers = []


        answers = data['other_qna_answers']
        for answer in answers:
            self.answers.append(ForumAnswer(clientrequests, answer))

    def answer(self, content):
        self.clientrequests.post(f"/qna/questions/{self.id}/answers", {"qna_answer": {"body": content, "qna_attachments_attributes": []}})