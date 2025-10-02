#!/usr/bin/env python3

from job import Job
from gui import GUI
import file_handling



class JobApplication:
    def __init__(self, data):
        super().__init__()
        self.data = data

   
if __name__ == "__main__":
    #app = JobApplication()
    gui = GUI()
    data = file_handling.load_data()
    if data == None:
       print("No data")
    else:
        parsed_data = [Job(**item) for item in data]   # convert the data into a Job object
        for i in parsed_data:
            print(i)
            
    test_data = file_handling.load_test_data()
    if test_data == None:
       print("No data")
    else:
        parsed_test_data = [Job(**item) for item in test_data]   # convert the data into a Job object
        # for value in test_data:
        #     if value["title"] == "Barman":
        #         print(value)
        filtered_dict = [job for job in parsed_test_data if job.title == "Barman"]
        for job in filtered_dict:
            print(f"Title: {job.title}, Description: {job.description}, Company: {job.company}")
    
    gui.run()