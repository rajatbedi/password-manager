import json
from tkinter import messagebox
import pyperclip


class SearchData:
    def __init__(self, website):
        try:
            with open("data.json", "r") as data_file:
                # read file
                data_dict = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message="No record Found")
        else:
            if website in data_dict:
                email = data_dict[website]["email"]
                password = data_dict[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)
            else:
                messagebox.showwarning(title="Oops", message=f"No details for the {website} exists")