import os
import json
import hashlib
from getpass import getpass
from utils import load_config, save_config, generate_key

CONFIG_FILE = "config.json"

def authenticate():
    if not os.path.exists(CONFIG_FILE):
        print("Setting up for first use...")
        salt = os.urandom(16)
        master_password = getpass("Create a master password: ")
        hashed = hashlib.pbkdf2_hmac("sha256", master_password.encode(), salt, 100000)
        key = generate_key()
        save_config({"salt": salt.hex(), "hash": hashed.hex(), "fernet_key": key.decode()})
        print("Setup complete.")
        return True

    config = load_config()
    salt = bytes.fromhex(config['salt'])
    stored_hash = config['hash']
    input_password = getpass("Enter master password: ")
    test_hash = hashlib.pbkdf2_hmac("sha256", input_password.encode(), salt, 100000).hex()

    return test_hash == stored_hash