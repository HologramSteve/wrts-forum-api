import axios, { AxiosResponse } from 'axios';

class Client {
    private baseurl: string;
    private headers: Record<string, string>;
    private authToken: string | undefined;

    constructor(email: string, password: string) {
        this.baseurl = "https://api.wrts.nl/api/v3";

        this.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,nl;q=0.8",
            "cache-control": "no-cache",
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
        };

        this.post("/auth/get_token", { email, password }).then(res => {
            this.authToken = res.data.auth_token;
            this.headers["X-Auth-Token"] = this.authToken;
        });
    }

    private async get(url: string): Promise<{ raw: AxiosResponse; json: any }> {
        if (!url.startsWith("/")) {
            throw new Error("Please enter a valid field!");
        }

        const response = await axios.get(`${this.baseurl}${url}`, { headers: this.headers });
        return { raw: response, json: response.data };
    }

    private async post(url: string, payload: any): Promise<AxiosResponse> {
        if (!url.startsWith("/")) {
            throw new Error("Please enter a valid field!");
        }

        return await axios.post(`${this.baseurl}${url}`, payload, { headers: this.headers });
    }

    public async forumGetAll(range: number = 20): Promise<any> {
        const res = await this.get("/public/qna/questions/");
        let data = res.json.results;

        if (range < 1 || range > 20) {
            throw new Error("Invalid range");
        }

        data = data.slice(0, range);
        return data;
    }

    public async forumQuestionGet(id: string): Promise<any> {
        const response = await this.get(`/public/qna/questions/${id}`);
        return response.json;
    }

    public async forumQuestionAnswer(id: string, answer: string): Promise<AxiosResponse> {
        const res = await this.post(`/qna/questions/${id}/answers`, {
            qna_answer: { body: answer, qna_attachments_attributes: [] }
        });
        return res;
    }

    public async forumAnswerLike(id: string): Promise<AxiosResponse> {
        const res = await this.post(`/qna/answers/${id}/votes`, {});
        return res;
    }

    public async forumQuestionCreate(content: string, subjectId: number = 1): Promise<AxiosResponse> {
        const res = await this.post("/qna/questions", {
            qna_question: {
                contents: content,
                qna_attachments_attributes: [],
                subject_id: subjectId
            }
        });
        return res;
    }
}
