from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_write():
    """take the input's website, mail id, password from the GUI then write into text file"""
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!!!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password_entry.txt", "a") as data:
                # print(f"{website} | {email} | {password}")
                data.write(f"{website} | {email} | {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="white")

# create canvas to place image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_image = PhotoImage(file="logo.png")
# create image( x,y, image), x,y are place the image from center
canvas.create_image(100, 100, image=password_image, )
canvas.grid(column=1, row=0)

# column span in grid used to extend the widget to number of columns
website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)
# website input box
website_input = Entry(width=35)
# cursor will pop up in the entry by using focus method
website_input.focus()

website_input.grid(column=1, row=1, columnspan=2)

# email, username label
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)
# email entry box
email_input = Entry(width=35)
# example of email id
email_input.insert(0, "example@gmail.com")

email_input.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)
# password label
password_input = Entry(width=35)

password_input.grid(row=3, column=1, columnspan=2)

# generate password button
generate_button = Button(text="Generate Password", command=generate_password, width=14, bg="white")
generate_button.grid(column=1, row=4)

# add button
add_button = Button(text="Add", command=password_write, width=15, bg="white")
add_button.grid(column=2, row=4)

window.mainloop()
