import tkinter as tk
from tkinter import filedialog
import zipfile
import os

def unzip_folder():
    zip_file_path = filedialog.askopenfilename(filetypes=[("Zip Files", "*.zip")])
    if not zip_file_path:
        return  

    destination_folder = filedialog.askdirectory()
    if not destination_folder:
        return  

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    print(f"Unzipped {zip_file_path} to {destination_folder}")

root = tk.Tk()
root.title("Unzip Folder")

unzip_button = tk.Button(root, text="Select Zip File and Unzip", command=unzip_folder)
unzip_button.pack(pady=10)

root.mainloop()
