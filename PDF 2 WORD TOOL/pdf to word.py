from spire.doc import *
import tkinter as tk

root = tk.Tk()
root.geometry("300x420")
pdfTitle = tk.Label(root, text="Doc to pdf")
pdfTitle.grid(row=0,column=1)
pdfbtn= tk.Button(root, text="select file")
pdfbtn.grid(row=0, column=2)
root.mainloop()


# Create a Word document
document = Document()
# Load a DOCX file
document.LoadFromFile("write your pdf file name here.docx")
# Save the document to PDF
document.SaveToFile("PDF.pdf", FileFormat.PDF)
document.Close()
