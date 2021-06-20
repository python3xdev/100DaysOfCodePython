from tkinter import *

FONT = ('Comic Sans MS', 14, 'normal')


def calculate():
    miles = float(user_input.get())
    result = round(miles * 1.6, 2)
    result_text.config(text=str(result))


window = Tk()
window.title("Mile to Km")
# window.minsize(width= , height=)
window.config(padx=20, pady=20)

# Labels

miles_text = Label(text='Miles', font=FONT)
miles_text.grid(row=0, column=2)

is_equal_to_text = Label(text="is equal to", font=FONT)
is_equal_to_text.grid(row=1, column=0)

result_text = Label(text="0", font=FONT)
result_text.grid(row=1, column=1)

km_text = Label(text="Km", font=FONT)
km_text.grid(row=1, column=2)

# Buttons

calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(row=2, column=1)

# Entry Fields

user_input = Entry(width=9)
user_input.grid(row=0, column=1)

window.mainloop()
