"""A script to like all answers of the last 20 questions"""
from api import Client
from time import sleep
import sys

def replaceLastLine(text: str):
    print(text, end="\r")  # Print new text

def load_clients_from_file(filename: str) -> str:
    progress = 0
    clients = []
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" ")  # Split each line by space
            if len(parts) == 2:
                email, password = parts
                clients.append(Client(email, password))
                progress += 1
                replaceLastLine(f"Loading accounts |{'=' * (round(progress / 6 * 10))}|")
            else:
                print("Warning: invalid account data line")
    return clients

accounts = load_clients_from_file("accounts.txt")
print(f"Loaded {len(accounts)} accounts |=========|")

def main(accounts: list, liked: list) -> list:
    main_acc: Client = accounts[0]

    feed = main_acc.forum_get_all(20)
    questionids = []
    ans_count = 0
    ans_progress = 0
    newliked = liked
    succes = 0
    ignored = 0


    for question in feed:
        questionids.append(question["id"])
        questiondata = main_acc.forum_question_get(question["id"])
        for answer in questiondata["qna_question"]["other_qna_answers"]:
            ans_count += 1

    for id in questionids:
        questiondata = main_acc.forum_question_get(id)

        for answer in questiondata["qna_question"]["other_qna_answers"]:
            if answer["qna_votes_count"] != len(accounts):
                newliked.append(answer["id"])
 
                for account in accounts:
                    account.forum_answer_like(answer["id"])
                ans_progress += 1
                replaceLastLine(f"Liking answers ({ans_progress}/{ans_count}) |{'=' * (round(ans_progress / ans_count * 10))}|")
                succes += 1
            else:
                ans_progress += 1
                ignored += 1
    print(f"Finished liking\nTotal: {ans_count}\nSuccesful: {succes}\nIgnored: {ignored}")
    return newliked



liked = []

while True:
     print("Checking...")
     liked = main(accounts, liked)
     print("Finished check.")
     sleep(30)
