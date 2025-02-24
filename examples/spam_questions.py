from api import Client

def load_clients_from_file(filename: str):
    progress = 0
    clients = []
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" ")  # Split each line by space
            if len(parts) == 2:
                email, password = parts
                clients.append(Client(email, password))
                progress += 1
            else:
                print("Warning: invalid account data line")
    return clients

accounts = load_clients_from_file("accounts2.txt")
msg = input(f"Enter the message to spam with {len(accounts)} accounts\n> ")
times = int(input("How many times to send in total?\n> "))

while times > 0:
    for client in accounts:
        r = client.forum_question_create(msg)
        print(r)
        print(r.json())
        print("Sent question")
        times -= 1
