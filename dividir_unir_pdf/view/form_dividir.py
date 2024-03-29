import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from util.helpers import Helpers
from controller.dividir_functions import TrabajarPDF

help = Helpers()
pdf = TrabajarPDF()

class PDFDividerApp:
    def __init__(self, ventana_principal):
        
        self.rutaPDF = ''
        self.rutaGuardar = ''
        
        self.ventana_principal = ventana_principal  
        self.ventana = tk.Toplevel(self.ventana_principal)  
        self.ventana.title('Dividir PDFs')
        self.ventana.config(bg='#ffd6dc')
        self.ventana.geometry("500x350")
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,350,500) # height width
        self.ventana.protocol("WM_DELETE_WINDOW", self.on_close)  # Captura el evento de cierre

        # Titulo principal
        titulo = tk.Label(self.ventana, text="Dividir PDF", font=("Arial", 20, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=170,y=8)

        imagen = Image.open(help.leerConfig("imagenUnir", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        label = tk.Label(self.ventana)
        label.place(x=100, y=50)
        label.config(image=imagen_tk, bg="#ffd6dc")
        
        self.entry_filename = tk.Entry(self.ventana, width=24)
        self.entry_filename.place_forget()

        # Botón para seleccionar el archivo PDF
        self.select_file_button = tk.Button(self.ventana, text="Seleccionar archivo", font=("Arial", 10, "bold"), command=self.select_pdf_file, width=18, bg='#ff8a9a')
        self.select_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.select_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.select_file_button.place(x=180, y=70)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_file_label = tk.Label(self.ventana, text="Ruta del archivo PDF: ", font=("Arial", 8, "bold"), bg='#ffd6dc')
        self.selected_file_label.place(x=20, y=110)

        # Etiqueta para la instrucción
        self.num_pages = tk.Label(self.ventana, text="Número de páginas por PDF:", font=("Arial", 10, "bold"), bg='#ffd6dc')
        self.num_pages.place(x=70, y=150)

        # Cuadro de entrada para el número de páginas por PDF
        self.entry_pages_per_pdf = tk.Entry(self.ventana, width=10)
        self.entry_pages_per_pdf.place(x=270, y=150)

        # Botón para seleccionar la ubicación de guardado
        self.select_output_button = tk.Button(self.ventana, text="Seleccionar carpeta de guardado", font=("Arial", 10, "bold"), command=self.select_output_folder, width=28, bg='#ff8a9a', state="disabled")
        self.select_output_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.select_output_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.select_output_button.place(x=160, y=190)

        # Etiqueta para mostrar la ruta de la carpeta de salida
        self.output_label = tk.Label(self.ventana, text="Ruta de guardado: ", font=("Arial", 8, "bold"), bg='#ffd6dc')
        self.output_label.place(x=60, y=230)

        # Botón para dividir el archivo PDF
        self.divide_button = tk.Button(self.ventana, text="Dividir PDF", font=("Arial", 10, "bold"), command=self.divide_pdf, width=11, bg='#ff8a9a', state="disabled")
        self.divide_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.divide_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.divide_button.place(x=200, y=270)

        self.close_button = tk.Button(self.ventana, text="Cerrar", font=("Arial", 10, "bold"), command=self.on_close, width=8, bg='#ff8a9a')
        self.close_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.close_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.close_button.place(x=410, y=310)
        
        self.ventana.mainloop()

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, file_path)
        self.selected_file_label.config(text=f"Ruta del archivo PDF: {file_path}")
        self.select_output_button.config(state=tk.NORMAL)
        self.divide_button.config(state=tk.DISABLED)
        self.rutaPDF = file_path 
    
    def select_output_folder(self):
        output_folder = filedialog.askdirectory()
        self.output_folder = output_folder
        self.output_label.config(text=f"Ruta de salida: {output_folder}")
        self.divide_button.config(state=tk.NORMAL)
        self.rutaGuardar = output_folder 
    
    def divide_pdf(self):
        num_pages = int(self.entry_pages_per_pdf.get())
        rutaPDF = self.rutaPDF
        rutaGuardar = self.rutaGuardar

        pdf.divide_pdf(rutaPDF, rutaGuardar, num_pages)
    
    def on_close(self):
        self.ventana.destroy()  # Cierra la ventana de dividir PDF
        self.ventana_principal.deiconify()  # Muestra la ventana principal

if __name__ == "__main__":
    PDFDividerApp()
