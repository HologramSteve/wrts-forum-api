import requests
from Errors import InvalidClientError
import threading

def genHeaders(token):
    return {
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
  "x-session-id": "1e63d6ec-fa87-4b5b-816d-c08cbb091de6",
  "X-Auth-Token": token
}


class ClientRequests:
    def __init__(self, token=None, isCluster=False, tokens=None):
        if isCluster and tokens == None:
            raise InvalidClientError("Can't have a cluster without tokens.")
        
        if (not isCluster) and token == None:
            raise InvalidClientError("Can't have a singular client without token.")


        self.tokens = tokens
        self.token = token

        self.isCluster = isCluster
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
  "x-session-id": "1e63d6ec-fa87-4b5b-816d-c08cbb091de6",
  "X-Auth-Token": token
}
    
    def get(self, url):
        if not url[0] == "/":
            return "Please enter a valid field!"
        reponse = requests.get(f"{self.baseurl}{url}")
        if reponse.status_code != 200:
            print(f"[X] Failed to fetch {url}")
            print(reponse.json())
            return False

        return {"raw": reponse, "json": reponse.json()}


    def post(self, url, payload):
        if self.isCluster:
            threads = []
            for token in self.tokens:
                t = threading.Thread(target=lambda tok=token: requests.post(f"{self.baseurl}{url}", json=payload, headers=genHeaders(tok.token)))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()
            return
        else:
            if not url[0] == "/":
                return "Please enter a valid field!"
            response = requests.post(f"{self.baseurl}{url}", json=payload, headers=self.headers)

            return response