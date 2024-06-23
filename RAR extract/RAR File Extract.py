import tkinter as tk
from tkinter import filedialog
import rarfile

def unrar_folder():
    rar_file_path = filedialog.askopenfilename(filetypes=[("RAR Files", "*.rar")])
    if not rar_file_path:
        return  
    destination_folder = filedialog.askdirectory()
    if not destination_folder:
        return 

    with rarfile.RarFile(rar_file_path, 'r') as rar_ref:
        rar_ref.extractall(destination_folder)

    print(f"Extracted {rar_file_path} to {destination_folder}")


root = tk.Tk()
root.title("Unrar Folder")

unrar_button = tk.Button(root, text="Select RAR File and Extract", command=unrar_folder)
unrar_button.pack(pady=10)

root.mainloop()
