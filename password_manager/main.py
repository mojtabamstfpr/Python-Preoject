import json
import getpass
passwords = {}
def save_passwords():
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)
def load_passwords():
    global passwords
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
load_passwords()
while True:
    action = input("add/view/exit: ")
    if action == "add":
        site = input("Enter site: ")
        pwd = getpass.getpass("Enter password: ")
        passwords[site] = pwd
        save_passwords()
    elif action == "view":
        print(passwords)
    elif action == "exit":
        break