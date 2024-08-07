from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave ant fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                              f" \n Password: {password} \n Is ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "siamak.kamanabroo@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
