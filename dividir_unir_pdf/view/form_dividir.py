import tkinter as tk
from tkinter import *
from controller.dividir_functions import divide_pdf, select_pdf_file, select_output_folder
class PDFDividerApp:
    def __init__(self, ventana):
        ventana = tk.Tk()  
        ventana = Toplevel(ventana)
        # Cuadro de entrada para el nombre del archivo PDF
        entry_filename = tk.Entry(ventana, width=40)
        entry_filename.grid(row=0, column=0, padx=10, pady=10)

        # Botón para seleccionar el archivo PDF
        select_file_button = tk.Button(ventana, text="Seleccionar PDF", command=select_pdf_file)
        select_file_button.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        selected_file_label = tk.Label(ventana, text="Ruta del archivo PDF: ")
        selected_file_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Cuadro de entrada para el número de páginas por PDF
        entry_pages_per_pdf = tk.Entry(ventana, width=10)
        entry_pages_per_pdf.grid(row=2, column=0, padx=10, pady=10)

        # Etiqueta para la instrucción
        tk.Label(ventana, text="Número de páginas por PDF").grid(row=2, column=1, padx=10, pady=10)

        # Botón para seleccionar la ubicación de guardado
        select_output_button = tk.Button(ventana, text="Seleccionar Carpeta de Salida", command=select_output_folder)
        select_output_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta para mostrar la ruta de la carpeta de salida
        output_label = tk.Label(ventana, text="Ruta de salida: ")
        output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Botón para dividir el archivo PDF
        divide_button = tk.Button(ventana, text="Dividir PDF", command=divide_pdf)
        divide_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        ventana.mainloop()
if __name__ == "__main__":
    PDFDividerApp()
