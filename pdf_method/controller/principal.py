import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from util.Helpers import Helpers
import os

help = Helpers()

class Visualizador:
    def __init__(self):
        # Crear una ventana de Tkinter
        self.ventana = tk.Tk()
        self.ventana.title('Dividir PDF')
        self.ventana.config(bg='#ffd6dc')
        self.ventana.configure(width=500, height=400)  # configura tamaño y altura de la ventana
        self.ventana.geometry("500x300")  # Especificar el tamaño de la ventana
        self.ventana.resizable(False,False)
        help.centerWindows(self.ventana,400,500) # height width
        
        # Titulo principal
        titulo = tk.Label(self.ventana, text="Dιʋιԃιɾ PDF", font=("Arial", 20, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=170,y=8)

        # Crea un cuadro de entrada para el nombre del archivo PDF
        self.entry_filename = tk.Entry(self.ventana, width=24)
        self.entry_filename.place(x=175, y=60)

        # Crea un botón para seleccionar el archivo PDF
        button_select_file = tk.Button(self.ventana, text="𝙎𝙚𝙡𝙚𝙘𝙘𝙞𝙤𝙣𝙖𝙧 𝙖𝙧𝙘𝙝𝙞𝙫𝙤", command=self.select_file, width=18, bg='#ff8a9a')
        button_select_file.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_select_file.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_select_file.place(x=180, y=120)

        # Crea un cuadro de entrada para el número de páginas por PDF
        self.entry_pages_per_pdf = tk.Entry(self.ventana, width=24)
        self.entry_pages_per_pdf.place(x=175, y=180)

        # Dando una instrucción
        mensaje = tk.Label(self.ventana, text="Cuantas paginas quieres dividir", font=("Arial", 12, "bold"), foreground="#f7072b", bg="#ffd6dc")
        mensaje.place(x=130, y=205)

        # Crea un botón para dividir el archivo PDF
        button_split_pdf = tk.Button(self.ventana, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", command=self.split_pdf, width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=180, y=260)
        
        button_merge_pdf = tk.Button(self.ventana, text="𝙐𝙣𝙞𝙧 𝙋𝘿𝙁", command=self.merge_pdfs, width=18, height=1, bg='#ff8a9a')
        button_merge_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_merge_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_merge_pdf.place(x=320, y=260)
        
        # Crea un boton para salir
        button_split_pdf = tk.Button(self.ventana, text="𝙎𝙖𝙡𝙞𝙧", command=self.salir, width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=320, y=360)
        
        self.ventana.mainloop()
        
    def salir(self):
        respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir de la aplicación?")
        if respuesta:
            self.ventana.destroy()

# Función para seleccionar el archivo PDF
    def select_file(self):
        # Abre un cuadro de diálogo para seleccionar el archivo PDF
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        # Asigna el nombre del archivo PDF al cuadro de entrada
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, filename)



    # Función para dividir el archivo PDF
    def split_pdf(self):
        filename = self.entry_filename.get()
        pages_per_pdf = self.entry_pages_per_pdf.get()

        try:
            # Abrir el archivo PDF
            pdf = PdfReader(open(filename, "rb"))

            # Obtener el número total de páginas del archivo PDF
            total_pages = len(pdf.pages)

            # Validar que el número de páginas por PDF sea un número entero positivo
            if not pages_per_pdf.isdigit() or int(pages_per_pdf) <= 0:
                messagebox.showerror("Error", "Por favor, ingresa un número válido de páginas por PDF.")
                return

            pages_per_pdf = int(pages_per_pdf)

            # Abre un cuadro de diálogo para seleccionar la ubicación de guardado
            output_directory = filedialog.askdirectory(title="Selecciona la carpeta de guardado")

            if not output_directory:
                messagebox.showerror("Error", "Debes seleccionar una carpeta de guardado.")
                return

            # Dividir el archivo PDF en partes iguales
            for i in range(0, total_pages, pages_per_pdf):
                # Crear un objeto PDFWriter para el archivo PDF de salida
                writer = PdfWriter()

                # Agregar las páginas al archivo PDF de salida
                for j in range(i, min(i + pages_per_pdf, total_pages)):
                    writer.add_page(pdf.pages[j])

                # Construir la ruta completa para el archivo de salida en la carpeta seleccionada
                output_filename = os.path.join(output_directory, f"{os.path.basename(filename)}_{i // pages_per_pdf + 1}.pdf")
                
                # Guardar el archivo PDF de salida
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)

            messagebox.showinfo("PDF dividido", "El proceso de división de PDF se ha completado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al dividir el PDF: {str(e)}")


    def merge_pdfs(self):
        # Abre un cuadro de diálogo para seleccionar los archivos PDF a unir
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

        if not file_paths:
            messagebox.showerror("Error", "Debes seleccionar al menos dos archivos PDF para unir.")
            return

        try:
            # Abre un cuadro de diálogo para seleccionar la ubicación de guardado
            output_directory = filedialog.askdirectory(title="Selecciona la carpeta de guardado")

            if not output_directory:
                messagebox.showerror("Error", "Debes seleccionar una carpeta de guardado.")
                return

            # Crear un objeto PDFWriter para el archivo PDF de salida
            merged_pdf = PdfWriter()

            # Agregar las páginas de cada archivo PDF al PDF de salida
            for file_path in file_paths:
                pdf = PdfReader(open(file_path, "rb"))
                for page in pdf.pages:
                    merged_pdf.add_page(page)

            # Construir la ruta completa para el archivo de salida en la carpeta seleccionada
            output_filename = os.path.join(output_directory, "merged_pdf.pdf")

            # Guardar el archivo PDF de salida en la carpeta seleccionada
            with open(output_filename, "wb") as output_file:
                merged_pdf.write(output_file)

            messagebox.showinfo("PDF unido", "El proceso de unión de PDFs se ha completado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al unir los PDFs: {str(e)}")

if __name__ == "__main__":
    Visualizador()