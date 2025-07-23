import requests
from Errors import TokenInvalidError
from Base.ClientRequests import *
from Classes import ForumManager
from Classes import GroupManager
from Base.ClientAuth import ClientAuth
import threading


class ClientCluster:
    def post(self, url: str, payload):
        if not url[0] == "/":
            return "Please enter a valid field!"
        response = requests.post(f"{self.baseurl}{url}", json=payload, headers=self.headers)

        return response
    def __init__(self, credentials):
        self.baseurl = "https://api.wrts.nl/api/v3"
        self.tokens = []

        threads = []
        lock = threading.Lock()

        for account in credentials:
            def worker(acc=account):  # default arg to capture current value
                username, password = acc.split(":")
                token = ClientAuth(username, password)
                with lock:
                    self.tokens.append(token)

            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
                    

        self.ClientRequests = ClientRequests(tokens=self.tokens, isCluster=True)

        # Client properties
        self.Forum = ForumManager.ForumManager(self.ClientRequests)
        self.GroupManager = GroupManager.GroupManager(self.ClientRequests)


        print("[V] Logged in to ClientCluster")

        # Events!

# Gebruik
# /groups/CODE/request_to_join (POST, geen payload),
# om een group te joinen.