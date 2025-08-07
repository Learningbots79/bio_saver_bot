import json

DATA_FILE = "bios.json"

def load_bios():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_bios(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def delete_bios(user_id):
    data = load_bios()
    if str(user_id) in data:
        del data[str(user_id)]
        save_bios(data)
        return True
    return False

def get_bios(user_id):
    data = load_bios()
    return data.get(str(user_id))

def set_bios(user_id, bio_text):
    data = load_bios()
    data[str(user_id)] = bio_text
    save_bios(data)
