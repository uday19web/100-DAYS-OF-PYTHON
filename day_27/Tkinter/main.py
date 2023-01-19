import tkinter

# creating window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# creating label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# pack method will display the label in the window
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)


# we will update the particular create for example text
my_label["text"] = "new text"
my_label.config(font=("Courier", 33, "underline"))

# create function for the button
def button_clicked():
    # my_label["text"] = "I got clicked"
    my_label["text"] = input.get()

# button
button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
button.config(pady=30, padx=40)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry class used for the input
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
print(input.get())


window.mainloop()