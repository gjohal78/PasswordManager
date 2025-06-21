import json
from cryptography.fernet import Fernet

CONFIG_FILE = "config.json"

def generate_key():
    return Fernet.generate_key()

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)