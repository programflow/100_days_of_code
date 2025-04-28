from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import os
import pyperclip
import json



def clear_entries():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_new_password():
    # Password Generator Project


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for c in range(randint(8,10))]
    password_list += [choice(numbers) for c in range(randint(2,4))]
    password_list += [choice(symbols) for c in range(randint(2,4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



    #---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website =website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if valid_entries():
        new_login = {
            website: [
                {
                "email": email,
                "password": password
            }
            ]
        }

        try:
            with open('login_data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_login)
            with open('login_data.json', 'w') as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Success", message="Login Successfully saved")
        except:
            messagebox.showinfo("New file Created", "New File Created")
            with open('login_data.json', 'w') as file:
                json.dump(new_login, file, indent=4)
                messagebox.showinfo(title="Success", message="Login Successfully saved")



        clear_entries()
        # else:
        #     messagebox.showerror(title="Error", message="Login already saved")
    else:
        print(valid_entries())
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")



# -------------------------------Search for Existing Logins----------------------------- #
def search():
    try:
        with open('login_data.json', 'r') as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            if website in data:
                print(f"You have the following Login information for {website}:")
                message = f"You have the following Login information for {website}:"
                for i in range(len(data[website])):
                    email = data[website][i]['email']
                    password = data[website][i]['password']
                    message += f"\n{email}: {password}"

                messagebox.showinfo(title="Search Result", message=message)
            else:
                messagebox.showinfo(title="No Search results",message=f"{website} login doesn't exist")
    except:
        messagebox.showinfo(title="No Search results",message=f"{website} login doesn't exist")



# -------------------------------Check for Empy Entries----------------------------- #

def valid_entries():
    if len(website_entry.get().strip()) != 0:
        if len(email_entry.get().strip()) != 0:
            if len(password_entry.get().strip()) != 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels

website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", fg="black", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=24, justify="left")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.insert(0, "")
website_entry.focus()
email_entry = Entry(width=44, justify="left")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "<EMAIL>")
password_entry = Entry(width=24, justify="left")
password_entry.grid(row=3, column=1, sticky="w")
password_entry.insert(0, "")

#Buttons
search_button = Button(width=16, text="Search", justify="left", command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", justify="left", command=generate_new_password)
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(width=41, text="Add", justify="left", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
