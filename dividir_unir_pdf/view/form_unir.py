import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from util.helpers import Helpers
import os

help = Helpers()

class PDFUnirApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Unir PDFs')
        self.ventana.geometry("500x350")
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,350,500) # height width

        # Botón para seleccionar la carpeta con archivos PDF
        self.btn_select_folder = tk.Button(self.ventana, text="Seleccionar carpeta con PDFs", command=self.select_folder)
        self.btn_select_folder.pack(pady=20)

        # Etiqueta para mostrar la ruta de la carpeta seleccionada
        self.folder_path_label = tk.Label(self.ventana, text="", wraplength=400)
        self.folder_path_label.pack()

        # Botón para seleccionar la carpeta de destino
        self.btn_select_output_folder = tk.Button(self.ventana, text="Seleccionar carpeta de destino", command=self.select_output_folder, state=tk.DISABLED)
        self.btn_select_output_folder.pack(pady=10)

        # Etiqueta para mostrar la ruta de la carpeta de destino
        self.output_folder_label = tk.Label(self.ventana, text="", wraplength=400)
        self.output_folder_label.pack()

        # Botón para unir PDFs
        self.btn_unir_pdf = tk.Button(self.ventana, text="Unir PDFs", command=self.unir_pdf, state=tk.DISABLED)
        self.btn_unir_pdf.pack(pady=20)

        self.folder_path = None
        self.output_folder = None
        
        self.ventana.mainloop()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory(title="Selecciona la carpeta con archivos PDF")
        if self.folder_path:
            self.folder_path_label.config(text=f"Carpeta seleccionada: {self.folder_path}")
            self.btn_select_output_folder.config(state=tk.NORMAL)
            self.btn_unir_pdf.config(state=tk.DISABLED)
            self.output_folder_label.config(text="")

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory(title="Selecciona la carpeta de destino")
        if self.output_folder:
            self.output_folder_label.config(text=f"Carpeta de destino seleccionada: {self.output_folder}")
            self.btn_unir_pdf.config(state=tk.NORMAL)

    def unir_pdf(self):
        if self.folder_path and self.output_folder:
            try:
                # Obtener la lista de archivos PDF en la carpeta seleccionada
                pdf_files = [os.path.join(self.folder_path, filename) for filename in os.listdir(self.folder_path) if filename.endswith(".pdf")]

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
                output_filename = os.path.join(self.output_folder, "pdf_unido.pdf")

                # Guardar el archivo PDF de salida en la carpeta de destino
                with open(output_filename, "wb") as output_file:
                    merged_pdf.write(output_file)

                messagebox.showinfo("PDF unido", "El proceso de unión de PDFs se ha completado correctamente.")

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al unir los PDFs: {str(e)}")
        else:
            messagebox.showerror("Error", "Debes seleccionar una carpeta con archivos PDF y una carpeta de destino.")

if __name__ == "__main__":
    PDFUnirApp()
