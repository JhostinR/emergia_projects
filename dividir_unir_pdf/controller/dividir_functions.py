from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

class TrabajarPDF:
    def divide_pdf(self, rutaPDF, rutaGuardar, num_pages):
        pdf_reader = PdfReader(rutaPDF)
        total_pages = len(pdf_reader.pages)

        for i in range(0, total_pages, num_pages):
            pdf_writer = PdfWriter()
            for j in range(i, min(i + num_pages, total_pages)):
                pdf_writer.add_page(pdf_reader.pages[j])

            output_filename = os.path.join(rutaGuardar, f"{os.path.basename(rutaPDF)}_{i // num_pages + 1}.pdf")
            with open(output_filename, "wb") as output_file:
                pdf_writer.write(output_file)

        messagebox.showinfo("Éxito", "El PDF se ha dividido correctamente.")