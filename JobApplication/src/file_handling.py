import json
# Loads data into system. Should be called when application is started.
@staticmethod
def load_data():
    try:
        with open("data/jobs.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None
    
# Loads test data. Should be called manually.
@staticmethod
def load_test_data():
    try:
        with open("tests/jobs.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None
    
if __name__ == "__main__":
    pass