import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

class PDFDividerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Dividir PDF')

        # Cuadro de entrada para el nombre del archivo PDF
        self.entry_filename = tk.Entry(root, width=40)
        self.entry_filename.grid(row=0, column=0, padx=10, pady=10)

        # Botón para seleccionar el archivo PDF
        select_file_button = tk.Button(root, text="Seleccionar PDF", command=self.select_pdf_file)
        select_file_button.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_file_label = tk.Label(root, text="Ruta del archivo PDF: ")
        self.selected_file_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Cuadro de entrada para el número de páginas por PDF
        self.entry_pages_per_pdf = tk.Entry(root, width=10)
        self.entry_pages_per_pdf.grid(row=2, column=0, padx=10, pady=10)

        # Etiqueta para la instrucción
        tk.Label(root, text="Número de páginas por PDF").grid(row=2, column=1, padx=10, pady=10)

        # Botón para seleccionar la ubicación de guardado
        select_output_button = tk.Button(root, text="Seleccionar Carpeta de Salida", command=self.select_output_folder)
        select_output_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta para mostrar la ruta de la carpeta de salida
        self.output_label = tk.Label(root, text="Ruta de salida: ")
        self.output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Botón para dividir el archivo PDF
        divide_button = tk.Button(root, text="Dividir PDF", command=self.divide_pdf)
        divide_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, file_path)
        self.selected_file_label.config(text=f"Ruta del archivo PDF: {file_path}")

    def select_output_folder(self):
        output_folder = filedialog.askdirectory()
        self.output_folder = output_folder
        self.output_label.config(text=f"Ruta de salida: {output_folder}")

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

                output_filename = os.path.join(self.output_folder, f"output_{i // pages_per_pdf + 1}.pdf")
                with open(output_filename, "wb") as output_file:
                    pdf_writer.write(output_file)

            messagebox.showinfo("Éxito", "El PDF se ha dividido correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al dividir el PDF: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFDividerApp(root)
    root.mainloop()
