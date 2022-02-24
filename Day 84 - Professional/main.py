import tkinter

from PIL import Image as PIL_Image
from tkinter import *
from tkinter import filedialog

chosen_filepath = ''
save_dir = ''
watermark_location = ''


def get_multiple_choice(choice):
    global watermark_location
    watermark_location = choice


def watermark():
    if not (chosen_filepath and save_dir):
        done_label.configure(text="Please specify all the required information first!", fg="red")

    main_img = PIL_Image.open(chosen_filepath)

    watermark_img = PIL_Image.open('watermark.png')

    if watermark_location == "Top Left Corner":
        main_img.paste(watermark_img, (0, 0))  # Top L
    elif watermark_location == "Top Right Corner":
        main_img.paste(watermark_img, (main_img.size[0] - watermark_img.size[0], 0))  # Top R
    elif watermark_location == "Bottom Right Corner":
        main_img.paste(watermark_img, (main_img.size[0] - watermark_img.size[0], main_img.size[1] - watermark_img.size[1]))  # Bottom R
    elif watermark_location == "Bottom Left Corner":
        main_img.paste(watermark_img, (0, main_img.size[1] - watermark_img.size[1]))  # Bottom L

    main_img.save(f"{save_dir}/{save_file_name.get()}.png", "PNG", quality=100)

    # TODO - later allow the user to select a filetype to save to e.g: PNG, JPEG, JPG etc...

    save_file_name.configure(bg="lightgreen")
    done_label.configure(text="Done!", fg="lightgreen")


def browse_img_files():
    global chosen_filepath
    chosen_filepath = filedialog.askopenfilename(initialdir="/",
                                                 title="Select a File",
                                                 filetypes=[
                                                     ("PNG, JPEG, JPG files", "*.png *.jpeg *.jpg"),
                                                     # ("JPEG files", "*.jpeg*"),
                                                     # ("JPG files", "*.jpg*"),
                                                 ])
    if chosen_filepath:
        selected_file_label.configure(text=f"File Selected: {chosen_filepath}", fg="green")


def browse_save_dir():
    global save_dir
    save_dir = filedialog.askdirectory()

    if save_dir:
        selected_folder_label.configure(text=f"Directory/Folder Selected: {save_dir}", fg="green")


window = Tk()

window.title("Watermark Your Images!")
# window.geometry("600x300")
window.config(background="white")
window.resizable(0, 0)  # turn off resizing on both axes

# all code run over and over in here

selected_file_label = Label(window, text="No Image File Selected.", fg='red', bg='white')
selected_folder_label = Label(window, text="No Save Directory/Folder Selected.", fg='red', bg='white')

browse_file_button = Button(window, text="Browse for Image Files", command=browse_img_files)
browse_folder_button = Button(window, text="Browse for a Save Folder", command=browse_save_dir)

value_inside = tkinter.StringVar(window)
options_list = ['Top Left Corner', 'Top Right Corner', 'Bottom Left Corner', 'Bottom Right Corner']
value_inside.set('Bottom Right Corner')
watermark_location_menu = OptionMenu(window, value_inside, *options_list, command=get_multiple_choice)


save_file_name = Entry(window, bg="lightpink")

watermark_button = Button(window, text="Watermark", command=watermark)

done_label = Label(window, text="", fg="lightgreen", bg="white")

selected_file_label.grid(column=1, row=1)
selected_folder_label.grid(column=1, row=2)
browse_file_button.grid(column=1, row=3)
browse_folder_button.grid(column=1, row=4)
watermark_location_menu.grid(column=1, row=5)
save_file_name.grid(column=1, row=6)
watermark_button.grid(column=1, row=7)
done_label.grid(column=1, row=8)

window.mainloop()
