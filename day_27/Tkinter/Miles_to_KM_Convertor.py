import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# creating mile entry
mile_input = tkinter.Entry(width=10)
mile_input.grid(column=1, row=0)

# label for miles
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)


# create label for "is equal to"
equal = tkinter.Label(text="is equal to ")
equal.grid(column=0, row=1)


# create label for output
output = tkinter.Label(text="0")
output.grid(column=1, row=1)


# create label for KM
km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

def calc():
    mile_value = mile_input.get()
    km = round(float(mile_value) * 1.6, 0)
    output.config(text= f"{km}")
# create button for calculate
button = tkinter.Button(text="Calculate", command=calc)
button.grid(column=1, row=3)










window.mainloop()