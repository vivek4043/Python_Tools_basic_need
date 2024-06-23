# from pdf2docx import parse
# from typing import Tupl

# def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
#     """Converts PDF to DOCX"""
#     if pages:
#         pages = [int(i) for i in list(pages) if i.isnumeric()]
#     result = parse(pdf_file=input_file, docx_with_path=output_file, pages=pages)
#     summary = {
#         "File": input_file,
#         "Pages": str(pages),
#         "Output File": output_file
#     }
#     # Printing Summary
#     print("## Summary ########################################################")
#     print("\n".join(f"{i}: {j}" for i, j in summary.items()))
#     print("###################################################################")
#     return result

# if __name__ == "__main__":
#     import sys
#     input_file = sys.argv[1]
#     output_file = sys.argv[2]
#     convert_pdf2docx(input_file, output_file)

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
document.LoadFromFile("anjli.docx")
# Save the document to PDF
document.SaveToFile("PDF.pdf", FileFormat.PDF)
document.Close()

