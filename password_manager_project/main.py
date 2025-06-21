from auth import authenticate
from vault import Vault
from getpass import getpass

def main():
    if not authenticate():
        print("Authentication failed.")
        return

    vault = Vault()
    while True:
        print("\nOptions: [1] Add Password [2] Get Password [3] List Services [4] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            vault.add_password(service, username, password)
        elif choice == '2':
            service = input("Enter service name: ")
            entry = vault.get_password(service)
            if entry:
                print(f"Username: {entry['username']}, Password: {entry['password']}")
            else:
                print("Service not found.")
        elif choice == '3':
            print("Saved services:")
            for service in vault.list_services():
                print(f" - {service}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()