import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from docx2pdf import convert

def openfile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    convert(file.name, r'I:\CODING\Python Code\New folder')
    showinfo("Done", "File successfully converted!")

win = tk.Tk()
win.title("Word to PDF Converter TOOL App")

label = tk.Label(win, text="Choose a Word file:")
label.grid(row=40, column=20, padx=20, pady=20)

button = tk.Button(win, text="Convert to PDF", command=openfile)
button.grid(row=50, column=20, padx=20, pady=20)

win.mainloop()
