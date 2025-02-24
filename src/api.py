import requests

class Client:
    def __init__(self, email, password):
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
        res = self.post("/auth/get_token", payload={"email": email, "password": password})
        self.headers["X-Auth-Token"] = res.json()["auth_token"]

        success = res.json()["success"]

    def get(self, url):
        if not url[0] == "/":
            return "Please enter a valid field!"
        reponse = requests.get(f"{self.baseurl}{url}")

        return {"raw": reponse, "json": reponse.json()}


    def post(self, url, payload):
        if not url[0] == "/":
            return "Please enter a valid field!"
        response = requests.post(f"{self.baseurl}{url}", json=payload, headers=self.headers)

        return response

    def forum_get_all(self, range=20):
        res = self.get("/public/qna/questions/")
        data = res["json"]["results"]

        if range < 1 or range > 20:
            return "Invalid range"

        data = data[:range]

        return data
    
    def forum_question_get(self, id):
        response = self.get(f"/public/qna/questions/{id}")
        
        return response["json"]

    def forum_question_answer(self, id, answer):
        res = self.post(f"/qna/questions/{id}/answers", {"qna_answer": {"body": answer, "qna_attachments_attributes": []}})
        # res = res.json() (caused error)

        return res

    def forum_answer_like(self, id):
        res = self.post(f"/qna/answers/{id}/votes", {})
        # res = res.json() (caused error, no response from api)

        return res

    def forum_question_create(self, content, subject_id=1):
        res = self.post("/qna/questions", {"qna_question": {
            "contents": content,
            "qna_attachments_attributes": [],
            "subject_id": subject_id
        }})

        return res
