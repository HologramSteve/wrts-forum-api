from Classes.ForumPost import ForumPost

class ForumManager:
    def __init__(self, clientrequests):
        self.ClientRequests = clientrequests
    
    # Class methods
    def fetchForumPosts(self, limit:int=20):
        res = self.ClientRequests.get("/public/qna/questions")
        
        res = res['json']['results']
        # print(type(res))
        res = res[:limit]

        posts = []
        for post in res:
            postdata = self.fetchPost(post['id'])
            
            posts.append(postdata)
        
        return posts

    def fetchPost(self, id):
        res = self.ClientRequests.get("/public/qna/questions/" + id)
        res = res['json']

        # print("RES::")
        # print(res)

        return ForumPost(res, self.ClientRequests)