import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
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
        self.entry_nombre_archivo_salida = tk.Entry(self.ventana, width=24)
        help.centerWindows(self.ventana,400,500) # height width
        
        # Titulo principal
        titulo = tk.Label(self.ventana, text="Dιʋιԃιɾ PDF", font=("Arial", 20, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=170,y=8)

        # Crea un cuadro de entrada para el nombre del archivo PDF
        self.entry_filename = tk.Entry(self.ventana, width=24)
        self.entry_filename.place(x=175, y=60)

        # Crea un botón para seleccionar el archivo PDF
        button_select_file = tk.Button(self.ventana, text="𝗦𝗲𝗹𝗲𝗰𝗰𝗶𝗼𝗻𝗮𝗿 𝗮𝗿𝗰𝗵𝗶𝘃𝗼\n(Dividir PDF)", command=self.select_file, width=26, bg='#ff8a9a')
        button_select_file.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_select_file.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_select_file.place(x=155, y=120)

        # Crea un cuadro de entrada para el número de páginas por PDF
        self.entry_pages_pdf = tk.Entry(self.ventana, width=24)
        self.entry_pages_pdf.place(x=175, y=180)

        # Dando una instrucción
        mensaje = tk.Label(self.ventana, text="Cuantas paginas quieres dividir", font=("Arial", 12, "bold"), foreground="#f7072b", bg="#ffd6dc")
        mensaje.place(x=130, y=205)


        # Crea un botón para dividir el archivo PDF
        button_split_pdf = tk.Button(self.ventana, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", command=self.split_pdf, width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=80, y=260)
        
        # Crea un botón para dividir el archivo PDF
        button_bind_pdf = tk.Button(self.ventana, text="𝙐𝙣𝙞𝙧", command=self.bind_pdf, width=18, height=1, bg='#ff8a9a')
        button_bind_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_bind_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_bind_pdf.place(x=290, y=260)
        
        # Crea un boton para salir
        button_split_pdf = tk.Button(self.ventana, text="𝙎𝙖𝙡𝙞𝙧", command=self.salir, width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=340, y=360)
        
        self.ventana.mainloop()
        
# Metodo para salir del aplicativo
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
        pages_per_pdf = self.entry_pages_pdf.get()

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

            # Dividir el archivo PDF en partes iguales
            for i in range(0, total_pages, pages_per_pdf):
                # Crear un objeto PDFWriter para el archivo PDF de salida
                writer = PdfWriter()

                # Agregar las páginas al archivo PDF de salida
                for j in range(i, min(i + pages_per_pdf, total_pages)):
                    writer.add_page(pdf.pages[j])

                # Guardar el archivo PDF de salida con un nombre diferente
                output_filename = f"{filename}_({i // pages_per_pdf + 1}).pdf"
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)

            messagebox.showinfo("PDF dividido", "El proceso de división de PDF se ha completado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al dividir el PDF: {str(e)}")
        
    def bind_pdf(self):
        pdfs = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        nombre_archivo_salida = self.entry_nombre_archivo_salida.get()
    
        # Validar el nombre del archivo de salida
        if not nombre_archivo_salida.isalnum() or len(nombre_archivo_salida) < 3:
            messagebox.showerror("Error", "El nombre del archivo de salida debe ser un nombre alfanumérico de al menos 3 caracteres.")
            return
    
        # Unir los archivos PDF
        fusionador = PdfMerger()
        for pdf in pdfs:
            fusionador.append(open(pdf, 'rb'))
    
        with open(nombre_archivo_salida, 'wb') as salida:
            fusionador.write(salida)
    
        # Cerrar el archivo de salida
        salida.close()
    
        messagebox.showinfo("PDF unido", "El proceso de unión de PDF se ha completado correctamente.")

if __name__ == "__main__":
    Visualizador()