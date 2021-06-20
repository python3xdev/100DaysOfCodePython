from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    user = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please fill out all of the "
                                                             "fields before you can continue.")
    else:
        try:
            with open('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Checking if website is not in data.json file
            if website not in data:
                # Updating old data with new data
                data.update(new_data)
                with open('data.json', 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                messagebox.showinfo(title="New Account Saved", message="Your new account data has been saved.")
            else:
                messagebox.showwarning(title="Already Exists", message=f"The website '{website}' already exists.\n"
                                                                       f"Try searching for it to find the password.")
        finally:
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    if len(website) != 0:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                if website in data:
                    login_data = data[website]
                    login_email = login_data['email']
                    login_password = login_data['password']
                    pyperclip.copy(login_password)
                    messagebox.showinfo(title=website, message=f"Email/Username: {login_email}\n"
                                                               f"Password: {login_password}")
                else:
                    messagebox.showwarning(title="Nothing Found", message=f"No credentials were found for '{website}'."
                                                                          f"\nMake sure your spelling is correct.")
        except FileNotFoundError:
            messagebox.showwarning(title="Missing Data File", message="Data file not found.")
    else:
        messagebox.showwarning(title="Empty Field", message="Please do not leave the 'Website'"
                                                            " field empty.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# FIRST FIELD
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

# SECOND FIELD
email_user_label = Label(text="Email/Username:", font=FONT)
email_user_label.grid(column=0, row=2)

email_user_entry = Entry(width=51)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "dan@gmail.com")

# THIRD FIELD
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Generate password button

generate_btn = Button(text="Generate Password", command=generate_password, width=14)
generate_btn.grid(column=2, row=3)

# Add button

add_btn = Button(text="Add", command=save_password, width=43)
add_btn.grid(column=1, row=4, columnspan=2)

# Search Button

search_btn = Button(text="Search", command=search, width=14)
search_btn.grid(column=2, row=1)

window.mainloop()
