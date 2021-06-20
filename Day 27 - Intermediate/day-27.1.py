from tkinter import *

def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# LABEL
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
# my_label['text'] = 'New Text' # This is so you can change the text later on in the code
# my_label.config(text="New Text") # This does the same...

# BUTTON

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me Too")
new_button.grid(column=2, row=0)

# ENTRY
user_input = Entry()  # width=30
user_input.grid(column=3, row=3)

window.mainloop()
