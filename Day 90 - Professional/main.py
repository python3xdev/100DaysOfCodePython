import requests

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from tkinter import *
from tkinter import filedialog

chosen_filepath = ''
save_dir = ''


def read_pdf_file(pdf_location, save_audio_filename):  # https://pdfminersix.readthedocs.io/en/latest/tutorial/composable.html
    output_string = StringIO()
    with open(pdf_location, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    create_and_save_audio(output_string.getvalue(), save_audio_filename)


def create_and_save_audio(text="This is the default text.", save_filename="audiobook.mp3", save_loc=""):
    query = {
        "key": YOUR_API_KEY_FOR_VOICERSS.ORG,
        "src": text,
        "hl": "en-us",
        "c": "MP3"
    }

    response = requests.get("http://api.voicerss.org/", params=query)

    print(response.content)
    print("Status Code: " + str(response.status_code))
    print(f"{save_dir}/{save_filename}")

    with open(f"{save_dir}/{save_filename}", "wb") as file:
        file.write(response.content)
    print("DONE!")


def browse_pdf_files():
    global chosen_filepath
    chosen_filepath = filedialog.askopenfilename(initialdir="/",
                                                 title="Select a File",
                                                 filetypes=[
                                                     ("PDF files", ".pdf .PDF")
                                                 ])
    if chosen_filepath:
        selected_file_label.configure(text=f"File Selected: {chosen_filepath}", fg="green")
        browse_file_button.grid_forget()


def browse_save_dir():
    global save_dir
    save_dir = filedialog.askdirectory()

    if save_dir:
        selected_folder_label.configure(text=f"Save Directory Selected: {save_dir}", fg="green")
        browse_folder_button.grid_forget()


def convert_pdf_to_audio():
    if save_file_name.get():

        read_pdf_file(chosen_filepath, f"{save_file_name.get()}.mp3")

        save_file_name.configure(bg="lightgreen")
        done_label.configure(text="Done!", fg="lightgreen")


window = Tk()
window.title("PDF to Audio!")

selected_file_label = Label(window, text="No PDF File Selected.", fg='red', bg='white')
selected_folder_label = Label(window, text="No Save Directory Selected.", fg='red', bg='white')

browse_file_button = Button(window, text="Browse for PDF Files", command=browse_pdf_files)
browse_folder_button = Button(window, text="Browse for a Save Folder", command=browse_save_dir)

save_file_name = Entry(window, bg="lightpink")

convert_button = Button(window, text="Convert", command=convert_pdf_to_audio)

done_label = Label(window, text="", fg="lightgreen", bg="white")

selected_file_label.grid(column=1, row=1)
selected_folder_label.grid(column=1, row=2)
browse_file_button.grid(column=1, row=3)
browse_folder_button.grid(column=1, row=4)
save_file_name.grid(column=1, row=5)
convert_button.grid(column=1, row=6)
done_label.grid(column=1, row=7)

window.mainloop()
