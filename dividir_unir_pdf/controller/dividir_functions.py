from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

class TrabajarPDF:
    def divide_pdf(self):
        pdf_file = self.entry_filename.get()
        pages_per_pdf = self.entry_pages_per_pdf.get()

        if not pdf_file:
            messagebox.showerror("Error", "Por favor, selecciona un archivo PDF.")
            return

        if not pages_per_pdf.isdigit() or int(pages_per_pdf) <= 0:
            messagebox.showerror("Error", "Por favor, ingresa un número válido de páginas por PDF.")
            return

        pages_per_pdf = int(pages_per_pdf)

        if not hasattr(self, 'output_folder'):
            messagebox.showerror("Error", "Por favor, selecciona una carpeta de salida.")
            return

        try:
            pdf_reader = PdfReader(pdf_file)
            total_pages = len(pdf_reader.pages)

            for i in range(0, total_pages, pages_per_pdf):
                pdf_writer = PdfWriter()
                for j in range(i, min(i + pages_per_pdf, total_pages)):
                    pdf_writer.add_page(pdf_reader.pages[j])

                output_filename = os.path.join(self.output_folder, f"{os.path.basename(pdf_file)}_{i // pages_per_pdf + 1}.pdf")
                with open(output_filename, "wb") as output_file:
                    pdf_writer.write(output_file)

            messagebox.showinfo("Éxito", "El PDF se ha dividido correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al dividir el PDF: {str(e)}")
