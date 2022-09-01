import json
from os.path import exists



# load from file to list contacts
def load(DATA_FILE):
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        save(DATA_FILE,[])
        return []


# save contacts list to a file
def save(DATA_FILE,contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f)
