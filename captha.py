import requests
import time

def solve(key, url, client_key):
    """
    Solve Google reCAPTCHA v2 using CapMonster.

    Args:
        key (str): The sitekey from the target page (reCAPTCHA site key).
        url (str): The URL of the page where captcha appears.
        client_key (str): Your CapMonster API key.

    Returns:
        str: The captcha token if solved successfully, else None.
    """

    # Step 1: Create a task
    create_task_url = "https://api.capmonster.cloud/createTask"
    task_payload = {
        "clientKey": client_key,
        "task": {
            "type": "NoCaptchaTaskProxyless",
            "websiteURL": url,
            "websiteKey": key
        }
    }

    response = requests.post(create_task_url, json=task_payload)
    if response.status_code != 200:
        print("Failed to create task:", response.text)
        return None

    resp_json = response.json()
    if resp_json.get("errorId") != 0:
        print("Error creating task:", resp_json.get("errorDescription"))
        return None

    task_id = resp_json.get("taskId")
    print(f"Task created with ID: {task_id}")

    # Step 2: Poll for result
    get_result_url = "https://api.capmonster.cloud/getTaskResult"
    result_payload = {
        "clientKey": client_key,
        "taskId": task_id
    }

    print("Waiting for captcha to be solved...")
    while True:
        time.sleep(5)  # wait before polling

        res = requests.post(get_result_url, json=result_payload)
        if res.status_code != 200:
            print("Failed to get task result:", res.text)
            return None

        res_json = res.json()
        if res_json.get("errorId") != 0:
            print("Error getting task result:", res_json.get("errorDescription"))
            return None

        if res_json.get("status") == "processing":
            print("Still processing...")
            continue

        if res_json.get("status") == "ready":
            solution = res_json.get("solution", {}).get("gRecaptchaResponse")
            print("Captcha solved!")
            return solution

