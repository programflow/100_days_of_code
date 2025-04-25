from tkinter import *
from tkinter import messagebox

def clear_entries():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website =website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_ok = messagebox.askokcancel(title=website, password=password)
    new_login_data = f"{website} | {email} | {password}\n"

    if not login_already_saved(new_login_data.strip()):




        with open("login_data.txt", "a") as file:
            file.write(new_login_data)
        clear_entries()
        messagebox.showinfo(title="Success", message="Login Successfully saved")
    else:
        messagebox.showerror(title="Error", message="Login already saved")


# ---------------------------- CHECK IF PASSWORD DATA ALREADY EXISTS ------------------------------- #
def login_already_saved(new_login_data):
    with open("login_data.txt", "r") as file:
        login_info = file.readlines()

    for login in login_info:
        if login.strip() == new_login_data:
            return True
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
website_entry = Entry(width=44, justify="left")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=44, justify="left")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "<EMAIL>")
password_entry = Entry(width=24, justify="left", show="*")
password_entry.grid(row=3, column=1, sticky="w")

#Buttons
generate_password_button = Button(text="Generate Password", justify="left")
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(width=41, text="Add", justify="left", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
