import requests
from Errors import TokenInvalidError
from Base.ClientRequests import *
from Classes import ForumManager
from Classes import GroupManager

class Client:
    def post(self, url: str, payload):
        if not url[0] == "/":
            return "Please enter a valid field!"
        response = requests.post(f"{self.baseurl}{url}", json=payload, headers=self.headers)

        return response
    def __init__(self, email: str, password: str):
        self.baseurl = "https://api.wrts.nl/api/v3"

        self.headers = {
  "accept": "application/json, text/plain, */*",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "en-US,en;q=0.9,nl;q=0.8",
  "cache-control": "no-cache",
  "content-length": "68",
  "content-type": "application/json",
  "origin": "https://studygo.com",
  "pragma": "no-cache",
  "priority": "u=1, i",
  "referer": "https://studygo.com/",
  "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "cross-site",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
  "x-client-type": "web",
  "x-device-id": "a46e6264-9f44-47e7-8c0c-c639af757a84",
  "x-language-code": "nl",
  "x-locale-code": "nl-NL",
  "x-session-id": "1e63d6ec-fa87-4b5b-816d-c08cbb091de6"
}
        res: requests.Response = self.post("/auth/get_token", payload={"email": email, "password": password})
        try:
            self.headers["X-Auth-Token"] = res.json()["auth_token"]
        except KeyError:
            raise TokenInvalidError(f"Log in information invalid. Email: {email}, password: {password}")
            
        self.token = res.json()["auth_token"]

        success = res.json()["success"]
        self.ClientRequests = ClientRequests(self.token)

        # Client properties
        self.Forum = ForumManager.ForumManager(self.ClientRequests)
        self.GroupManager = GroupManager.GroupManager(self.ClientRequests)


        print("[V] Logged in to Client")

        # Events!

# Gebruik
# /groups/CODE/request_to_join (POST, geen payload),
# om een group te joinen.