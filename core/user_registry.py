import json, os
from cryptography.fernet import Fernet
from core.config import FERNET_KEY

cipher = Fernet(FERNET_KEY)
DB_PATH = "data/user_registry.json"

def _load():
    return json.load(open(DB_PATH)) if os.path.exists(DB_PATH) else {}

def _save(data):
    json.dump(data, open(DB_PATH, "w"), indent=2)

def add_user(user_id, value):
    data = _load()
    data[user_id] = cipher.encrypt(value.encode()).decode()
    _save(data)

def get_user(user_id):
    data = _load()
    if user_id in data:
        return cipher.decrypt(data[user_id].encode()).decode()
    return None
