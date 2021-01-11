from tkinter import messagebox
import json


class SaveData:
    def __init__(self, website, email, password):
        new_data = {
            website: {
                "email": email, "password": password
            }
        }
        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showwarning(title="Oops", message="Please fill all the inputs")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # read file
                    data = json.load(data_file)
            except FileNotFoundError:
                # write data
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # update data
                data.update(new_data)
                # write data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
