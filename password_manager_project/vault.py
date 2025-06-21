import json
import os
from cryptography.fernet import Fernet
from utils import load_config

VAULT_FILE = "vault.json"

class Vault:
    def __init__(self):
        config = load_config()
        self.fernet = Fernet(config["fernet_key"].encode())
        if not os.path.exists(VAULT_FILE):
            with open(VAULT_FILE, "w") as f:
                json.dump({}, f)

    def load_vault(self):
        with open(VAULT_FILE, "r") as f:
            encrypted_data = f.read()
            if not encrypted_data:
                return {}
            return json.loads(self.fernet.decrypt(encrypted_data.encode()).decode())

    def save_vault(self, data):
        encrypted_data = self.fernet.encrypt(json.dumps(data).encode()).decode()
        with open(VAULT_FILE, "w") as f:
            f.write(encrypted_data)

    def add_password(self, service, username, password):
        data = self.load_vault()
        data[service] = {"username": username, "password": password}
        self.save_vault(data)
        print("Password added.")

    def get_password(self, service):
        data = self.load_vault()
        return data.get(service)

    def list_services(self):
        return list(self.load_vault().keys())