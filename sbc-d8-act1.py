def read_users():
    try:
        with open("users.txt", "r") as file:
            users = {}
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
            return users
    except FileNotFoundError:
        return {}

def write_users(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")

def register():
    users = read_users()
    username = input("Username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return
    password = input("Password: ")
    users[username] = password
    write_users(users)
    print("Registration successful!")

def login():
    users = read_users()
    username = input("Username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return
    password = input("Password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")

def change_password():
    users = read_users()
    username = input("Username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return
    old_password = input("old password: ")
    if users[username] == old_password:
        new_password = input("New password: ")
        users[username] = new_password
        write_users(users)
        print("Password changed successfully!")
    else:
        print("Incorrect old password. Please try again.")

def main():
    while True:
        print("\nOptions: register, login, change_password, exit")
        choice = input("Choose an option: ").strip().lower()
        if choice == 'register':
            register()
        elif choice == 'login':
            login()
        elif choice == 'change_password':
            change_password()
        elif choice == 'exit':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()                           