# WIN-1-21. Estate agency. Team members: Zulfibaeva Bermet, Nogorbekov Salim, Rapilbekova Akylai

import json
print("Estate agency 'SAB' is greeting you!")

# load database with extension json
with open("marketing_db.json") as file:
    try:
        marketing_db = json.load(file)
    except json.decoder.JSONDecodeError:
        marketing_db = {}
with open("director_db.json") as file:
    try:
        director_db = json.load(file)
    except json.decoder.JSONDecodeError:
        director_db = {}
with open("manager_db.json") as file:
    try:
        manager_db = json.load(file)
    except json.decoder.JSONDecodeError:
        manager_db = {}
with open("worker_db.json") as file:
    try:
        worker_db = json.load(file)
    except json.decoder.JSONDecodeError:
        worker_db = {}
with open("sale-manager_db.json") as file:
    try:
        sale_manager_db = json.load(file)
    except json.decoder.JSONDecodeError:
        sale_manager_db = {}

# validate_password
def validate_password(account_db, account_type, login, password):
    if account_db.get(login):
        if account_db[login] == password:
            print("Success!")
            print("Greatings Dear", account_type)
            if account_type == "marketer":
                import m
                m.m()
            elif account_type == "director":
                import d
                d.d()
            elif account_type == "manager":
                import man
                man.man()
            elif account_type == "worker":
                import w
                w.work()
            elif account_type == "sale-manager":
                import s
                s.s()
        else:
            print("Password is not found!")
            main()
    else:
        print(f"This user does not exist!")
        main()

# login
def check_account(account_type, login, password):
    if account_type == 'marketer':
        validate_password(marketing_db, account_type, login, password)
    elif account_type == 'director':
        validate_password(director_db, account_type, login, password)
    elif account_type == 'manager':
        validate_password(manager_db, account_type, login, password)
    elif account_type == 'worker':
        validate_password(worker_db, account_type, login, password)
    elif account_type == 'sale-manager':
        validate_password(sale_manager_db, account_type, login, password)
    else:
        print("This type of account does not exist!")
        main()

# register.Check registration.
def register_account(account_type, login, password, password_confirm):
    if password != password_confirm:
        print("Password mismatch!")
        main()
        return

    if account_type == 'marketer':
        marketing_db[login] = password
        with open("marketing_db.json", 'w') as file:
            json.dump(marketing_db, file)
    elif account_type == 'director':
        director_db[login] = password
        with open("director_db.json", 'w') as file:
            json.dump(director_db, file)
    elif account_type == 'manager':
        manager_db[login] = password
        with open("manager_db.json", 'w') as file:
            json.dump(manager_db, file)
    elif account_type == 'worker':
        worker_db[login] = password
        with open("worker_db.json", 'w') as file:
            json.dump(worker_db, file)
    elif account_type == 'sale-manager':
        sale_manager_db[login] = password
        with open("sale_manager_db.json", 'w') as file:
            json.dump(sale_manager_db, file)
    else:
        print("This type of account does not exist!")
        main()

# registration/authorisation
def main():
    account_type = input("Enter your type of account\n(marketer, director, manager, worker, sale-manager):\n").lower().replace(" ", '')
    enter = input("Log in or Register? (l/r): ").lower().strip()
    login = input("Login: ")
    password = input("Password: ")
    if enter == 'l':
        check_account(account_type, login, password)
    elif enter == 'r':
        password_confirm = input("Confirm Password: ")
        register_account(account_type, login, password, password_confirm)
        return main()
main()






