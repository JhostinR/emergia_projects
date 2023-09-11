import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from util.helpers import Helpers
import os

help = Helpers()

class PDFUnirApp:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal  
        self.ventana = tk.Toplevel(self.ventana_principal) 
        self.ventana.title('Unir PDFs')
        self.ventana.geometry("500x350")
        self.ventana.config(bg='#ffd6dc')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,350,500) # height width
        
        # Titulo principal
        titulo = tk.Label(self.ventana, text="Unir PDF", font=("Arial", 20, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=190,y=8)
        
        imagen = Image.open(help.leerConfig("imagenUnir", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)
        
        label = tk.Label(self.ventana)
        label.place(x=100, y=50)
        label.config(image=imagen_tk, bg="#ffd6dc")

        # Botón para seleccionar la carpeta con archivos PDF
        self.btn_select_folder = tk.Button(self.ventana, text="Seleccionar carpeta con PDFs", font=("Arial", 10, "bold"), command=self.select_folder, bg='#ff8a9a')
        self.btn_select_folder.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.btn_select_folder.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.btn_select_folder.place(x=150, y=70)
        
        # Etiqueta para mostrar la ruta de la carpeta seleccionada
        self.folder_path_label = tk.Label(self.ventana, text="", wraplength=400, bg='#ffd6dc')
        self.folder_path_label.place(x=110,y=115)

        # Botón para seleccionar la carpeta de destino
        self.btn_select_output_folder = tk.Button(self.ventana, text="Seleccionar carpeta de destino", font=("Arial", 10, "bold"), command=self.select_output_folder, state=tk.DISABLED, bg='#ff8a9a')
        self.btn_select_output_folder.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.btn_select_output_folder.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.btn_select_output_folder.place(x=150, y=150)

        # Etiqueta para mostrar la ruta de la carpeta de destino
        self.output_folder_label = tk.Label(self.ventana, text="", wraplength=400, bg='#ffd6dc')
        self.output_folder_label.place(x=90,y=200)

        # Botón para unir PDFs
        self.btn_unir_pdf = tk.Button(self.ventana, text="Unir PDFs", command=self.unir_pdf, state=tk.DISABLED, font=("Arial", 10, "bold"), bg='#ff8a9a')
        self.btn_unir_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.btn_unir_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.btn_unir_pdf.place(x=215,y=250)

        self.folder_path = None
        self.output_folder = None
        
        close_button = tk.Button(self.ventana, text="Cerrar", command=self.on_close, font=("Arial", 11, "bold"), bg='#ff8a9a')
        close_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        close_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        close_button.place(x=400,y=300)
        
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
    
    def on_close(self):
        self.ventana.destroy()  # Cierra la ventana de dividir PDF
        self.ventana_principal.deiconify()  # Muestra la ventana principal

if __name__ == "__main__":
    PDFUnirApp()
