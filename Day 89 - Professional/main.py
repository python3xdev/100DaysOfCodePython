from tkinter import *
import time
import pyperclip as pc

total_time = 120
wipe_time_loop = None
start_time = 0
time_left = 0

first_time_loop = None
second_time_loop = None
third_time_loop = None
fourth_time_loop = None
fifth_time_loop = None

already_started = False

window = Tk()
window.title("The Most Dangerous Writing App")
# window.geometry("400x400")


def start_timer(event=None):
    global already_started, wipe_time_loop
    if not already_started:
        handle_wait()
        typing_area.bind("<Key>", handle_wait)
        global start_time
        start_time = time.time()
        display_time_left()
        already_started = True


def handle_wait(event=None):  # https://stackoverflow.com/a/37439232
    global wipe_time_loop, first_time_loop, second_time_loop, third_time_loop, fourth_time_loop, fifth_time_loop
    typing_area.config(bg="white")
    # cancel the old job
    if wipe_time_loop is not None:
        window.after_cancel(wipe_time_loop)
    if first_time_loop is not None:
        window.after_cancel(first_time_loop)
    if second_time_loop is not None:
        window.after_cancel(second_time_loop)
    if third_time_loop is not None:
        window.after_cancel(third_time_loop)
    if fourth_time_loop is not None:
        window.after_cancel(fourth_time_loop)
    if fifth_time_loop is not None:
        window.after_cancel(fifth_time_loop)

    # creating a new job
    if time_left > 0:
        first_time_loop = window.after(500, first_second)
        second_time_loop = window.after(1000, second_second)
        third_time_loop = window.after(2000, third_second)
        fourth_time_loop = window.after(3000, fourth_second)
        fifth_time_loop = window.after(4000, fifth_second)
        wipe_time_loop = window.after(5000, wipe_text)


def first_second():
    typing_area.config(bg="#fffafa")


def second_second():
    typing_area.config(bg="#ffe8e8")


def third_second():
    typing_area.config(bg="#ffd6d6")


def fourth_second():
    typing_area.config(bg="#ffbaba")


def fifth_second():
    typing_area.config(bg="#ff8787")


def wipe_text():
    typing_area.config(bg="white")
    typing_area.delete('1.0', 'end')
    reset()


def reset():
    global total_time, wipe_time_loop, start_time, already_started
    total_time = 120
    wipe_time_loop = None
    start_time = 0
    already_started = False

    if time_loop:
        window.after_cancel(time_loop)

    total_time_left_label.config(text=f"Total Time Left: {total_time}")

    typing_area.bind("<Key>", start_timer)


def display_time_left():
    global time_loop, time_left
    curr_time_past = int(time.time() - start_time)
    time_left = total_time - curr_time_past
    total_time_left_label.config(text=f"Total Time Left: {time_left}")
    if time_left == 0:
        users_text = typing_area.get('1.0', 'end')
        pc.copy(users_text)
        print("Your Text Has Been Copied To Your Clipboard:")
        print(users_text)
        typing_area.config(state='disabled')
        typing_area.delete(0, END)
    else:
        time_loop = window.after(1000, display_time_left)


total_time_left_label = Label(window, text=f"Total Time Left: {total_time}")
total_time_left_label.grid(column=1, row=1)

typing_area = Text(window)
typing_area.grid(column=1, row=3)

typing_area.bind("<Key>", start_timer)

window.mainloop()
