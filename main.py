from tkinter import *
from tkinter import messagebox
from generate_password import GeneratePassword
from search_data import SearchData
from save_data import SaveData


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    generate_password = GeneratePassword()
    pass_input.delete(0, END)
    pass_input.insert(0, generate_password.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    # save data
    SaveData(website, email, password)
    # clear Inputs
    website_input.delete(0, END)
    pass_input.delete(0, END)


# ---------------------------- Search Website ------------------------------- #
def search():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please enter a website")
    else:
        SearchData(website)


# ---------------------------- UI SETUP ------------------------------- #
display = Tk()
display.title("Password Manager")
display.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=54)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "rajatbedi0002@gmail.com")

pass_input = Entry(width=35)
pass_input.grid(row=3, column=1)

# buttons
generate_pass = Button(text="Generate Password", command=generate_pass)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

display.mainloop()
