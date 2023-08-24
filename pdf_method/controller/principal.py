from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
import PyPDF2

class Visualizador:
    def __init__(self):

# Crea una ventana de Tkinter
        ventana = tk.Tk()

# Crea un cuadro de entrada para el nombre del archivo PDF
        entry_filename = tk.Entry(ventana)
        entry_filename.pack()

# Crea un botón para seleccionar el archivo PDF
        button_select_file = tk.Button(ventana, text="Seleccionar archivo", command=lambda: self.select_file(entry_filename))
        button_select_file.pack()

# Crea un cuadro de entrada para el número de páginas por PDF
        entry_pages_per_pdf = tk.Entry(ventana)
        entry_pages_per_pdf.pack()

# Crea un botón para dividir el archivo PDF
        button_split_pdf = tk.Button(ventana, text="Dividir PDF", command=lambda: self.split_pdf(entry_filename.get(), entry_pages_per_pdf.get()))
        button_split_pdf.pack()

        ventana.mainloop()
    # Función para seleccionar el archivo PDF
        def select_file(entry):
            # Abre un cuadro de diálogo para seleccionar el archivo PDF
            filename = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
            # Asigna el nombre del archivo PDF al cuadro de entrada
            entry.delete(0, tk.END)
            entry.insert(0, filename)
    
    # Función para dividir el archivo PDF
        def split_pdf(filename, pages_per_pdf):
            # Crea un objeto PDFReader para el archivo PDF
            reader = PyPDF2.PdfReader(filename)
    
            # Obtiene el número total de páginas del archivo PDF
            total_pages = len(reader.pages)
    
            # Itera sobre el archivo PDF, dividiendo el archivo en PDF de páginas_per_pdf páginas cada uno
            for i in range(0, total_pages, int(pages_per_pdf)):
                # Crea un objeto PDFWriter para el archivo PDF de salida
                writer = PdfWriter()
    
                # Agrega las páginas del archivo PDF al archivo PDF de salida
                for page in reader.pages[i:min(i + int(pages_per_pdf), total_pages)]:
                    writer.add_page(page)
    
                # Escribe el archivo PDF de salida con el nombre editado
                with open("{}.pdf".format(filename), "wb") as output_file:
                    writer.write(output_file)
                
# Ejecuta el código
if __name__ == "__main__":
    Visualizador()