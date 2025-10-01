#!/usr/bin/env python3

import json

class JobApplication:
    def __init__(self, data):
        super().__init__()
        self.data = data

    # Loads data into system. Should be called when application is started.
    @staticmethod
    def load_data():
        try:
            with open("data/jobs.json", "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Error: The file was not found.")
        except json.decoder.JSONDecodeError:
            pass
        return None
    
    # Loads test data. Should be called manually.
    @staticmethod
    def load_test_data():
        try:
            with open("tests/jobs.json", "r") as file: 
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Error: The file was not found.")
        except json.decoder.JSONDecodeError:
            pass
        return None
        
if __name__ == "__main__":
    app = JobApplication([])
    data = app.load_data()
    if data == None:
       print("No data")
    else:
        for i in data:
            print(i)
            
    test_data = app.load_test_data()
    if test_data == None:
       print("No data")
    else:
        app.data = test_data
        # for i in app.data:
        #     print(i)
    
    for value in app.data:
        if value["title"] == "Barman":
            print(value)
    
    filtered_dict = {key: value for key, value in app.data if value["title"] == "Barman"}