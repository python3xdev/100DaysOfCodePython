import time
from tkinter import *
from random import shuffle
from words import all_words


def create_a_200_words_list():
    shuffle(all_words)
    new_200_words_list = all_words[:200]
    return new_200_words_list


start_time = 0
total_time = 60  # seconds
main_words = create_a_200_words_list()

total_words = 0
correct_words = 0
mistyped_words = 0
accuracy = 0

window = Tk()
window.title("Typing Speed Test")
window.geometry("350x500")


def start():
    start_button.grid_remove()
    typing_area.grid()
    typing_area.focus()
    retry_button.grid()
    words_label.config(text=' '.join(main_words))


def start_timer(key):
    typing_area.unbind("<Key>")
    global start_time
    start_time = time.time()
    display_time_left()


def display_time_left():
    global time_loop
    curr_time_past = int(time.time() - start_time)
    time_left = total_time - curr_time_past
    time_label.config(text=f"Time Left: {time_left}")
    if time_left == 0:
        typing_area.config(state='disabled')
        users_text = typing_area.get()
        check_results(users_text)
        typing_area.grid_remove()
        words_label.grid_remove()
        results_label.grid()
    else:
        time_loop = window.after(1000, display_time_left)


def check_results(user_input):
    global correct_words, mistyped_words, accuracy, total_words
    users_words = user_input.split()
    for word in users_words:
        if word in main_words:
            correct_words += 1
        else:
            mistyped_words += 1
        total_words += 1
    accuracy = round(1 - mistyped_words/total_words, 2) * 100

    results_label.config(text=f"Word Per Minute: {total_words}\nCorrect Words: {correct_words}\nMistyped Words: {mistyped_words}\nAccuracy: {round(accuracy, 2)}%")


def retry():
    global start_time, main_words, correct_words, mistyped_words, accuracy, total_words
    start_time = 0
    main_words = create_a_200_words_list()

    time_label.config(text=f"Time Left: {total_time}")

    total_words = 0
    correct_words = 0
    mistyped_words = 0
    accuracy = 0

    results_label.grid_remove()
    retry_button.grid_remove()

    words_label.grid()

    typing_area.config(state='normal')
    typing_area.delete(0, END)
    typing_area.grid()
    typing_area.focus()
    typing_area.bind("<Key>", start_timer)

    window.after_cancel(time_loop)  # so the time does not go crazy while clicking retry in the middle of a test...

    start()


time_label = Label(window, text=f"Time Left: {total_time}")
time_label.grid(column=1, row=1)

words_label = Label(window, text='', wraplength=300, justify="center")
words_label.grid(column=1, row=2)

typing_area = Entry(window, width=50)
typing_area.grid(column=1, row=3)
typing_area.bind("<Key>", start_timer)
typing_area.grid_remove()

results_label = Label(window, text='', justify="center")
results_label.grid(column=1, row=4)
results_label.grid_remove()

start_button = Button(window, text="Start", command=start)
start_button.grid(column=1, row=5)

retry_button = Button(window, text="Retry", command=retry)
retry_button.grid(column=1, row=6)
retry_button.grid_remove()

window.grid_columnconfigure(1, weight=1)

window.mainloop()
