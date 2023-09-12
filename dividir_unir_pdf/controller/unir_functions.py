import tkinter as tk
from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

class UnirPDF():
    def unir_pdf(self, output_folder, folder_path):
        if folder_path and output_folder:
            try:
                # Obtener la lista de archivos PDF en la carpeta seleccionada
                pdf_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".pdf")]

                if len(pdf_files) < 2:
                    messagebox.showerror("Error", "Debes tener al menos dos archivos PDF en la carpeta para unir.")
                    return

                # Crear un objeto PDFWriter para el archivo PDF de salida
                merged_pdf = PdfWriter()

                # Agregar las páginas de cada archivo PDF al PDF de salida
                for file_path in pdf_files:
                    pdf = PdfReader(file_path)
                    for page in pdf.pages:
                        merged_pdf.add_page(page)

                # Construir la ruta completa para el archivo de salida en la carpeta de destino
                output_filename = os.path.join(output_folder, "pdf_unido.pdf")

                # Guardar el archivo PDF de salida en la carpeta de destino
                with open(output_filename, "wb") as output_file:
                    merged_pdf.write(output_file)

                messagebox.showinfo("PDF unido", "El proceso de unión de PDFs se ha completado correctamente.")

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al unir los PDFs: {str(e)}")
        else:
            messagebox.showerror("Error", "Debes seleccionar una carpeta con archivos PDF y una carpeta de destino.")