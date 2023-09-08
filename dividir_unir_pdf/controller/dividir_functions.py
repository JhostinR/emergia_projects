import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def select_output_folder():
    output_folder = filedialog.askdirectory()
    return output_folder

def divide_pdf(pdf_file, pages_per_pdf, output_folder):
    if not pdf_file:
        raise Exception("Please select a PDF file.")

    if not pages_per_pdf.isdigit() or int(pages_per_pdf) <= 0:
        raise Exception("Please enter a valid number of pages per PDF.")

    pages_per_pdf = int(pages_per_pdf)

    if not output_folder:
        raise Exception("Please select an output folder.")

    try:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        for i in range(0, total_pages, pages_per_pdf):
            pdf_writer = PdfWriter()
            for j in range(i, min(i + pages_per_pdf, total_pages)):
                pdf_writer.add_page(pdf_reader.pages[j])

            output_filename = os.path.join(output_folder, f"output_{i // pages_per_pdf + 1}.pdf")
            with open(output_filename, "wb") as output_file:
                pdf_writer.write(output_file)

    except Exception as e:
        raise Exception(f"An error occurred while dividing the PDF: {str(e)}")