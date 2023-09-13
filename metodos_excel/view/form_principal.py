import tkinter as tk
from tkinter import filedialog
from util.helpers import Helpers
from PIL import Image, ImageTk
import pandas as pd

help = Helpers()

class Visualizador:
    def __init__(self):
        # Crear una ventana_principal de Tkinter
        self.ventana_principal = tk.Tk()
        super().__init__()
        self.ventana_principal.title('Dividir PDF')
        self.ventana_principal.config(bg='#fff')
        self.ventana_principal.configure(width=500, height=400)  # configura tamaño y altura de la ventana_principal
        self.ventana_principal.geometry("500x400")  # Especificar el tamaño de la ventana_principal
        self.ventana_principal.resizable(False,False)
        help.centerWindows(self.ventana_principal,400,500) # height width
        
        # Llama el icono de la ventana_principal
        logo = help.getImage("imagenPDF", (200, 200))
        self.ventana_principal.iconphoto(True, logo)
        
        imagen = Image.open(help.leerConfig("imagenPrincipal", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)
        
        label = tk.Label(self.ventana_principal)
        label.place(x=100, y=80)
        label.config(image=imagen_tk, bg="#fff")
        
        # Titulo principal
        titulo = tk.Label(self.ventana_principal, text="Dιʋιԃιɾ PDF", font=("Arial", 26, "bold"), foreground="#000", bg="#ffd6dc")
        titulo.place(x=150,y=8)

        self.entry_filename = tk.Entry(self.ventana_principal, width=24)
        self.entry_filename.place_forget()

        self.select_file_button = tk.Button(self.ventana_principal, text="Seleccionar archivo", font=("Arial", 10, "bold"), command=self.select_pdf_file, width=18, bg='#ff8a9a')
        self.select_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        self.select_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        self.select_file_button.place(x=180, y=70)
        
        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_file_label = tk.Label(self.ventana_principal, text="Ruta del archivo PDF: ", font=("Arial", 8, "bold"), bg='#ffd6dc')
        self.selected_file_label.place(x=20, y=110)

        self.label_rows = tk.Label(self.ventana_principal, text="pruebas", font=("Arial", 10, "normal"), bg='#ffd6dc')
        self.label_rows.place(x=20, y=150)
        
        self.ventana_principal.mainloop()

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, file_path)
        self.selected_file_label.config(text=f"Ruta del archivo PDF: {file_path}")

        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)

        # Print the first 5 rows
        # Add a new label to the GUI window
        label_rows = tk.Label(self.ventana_principal, text=df.head(5).to_string(), font=("Arial", 10, "normal"), bg='#ffd6dc')
        label_rows.place(x=20, y=150)

if __name__ == "__main__":
    Visualizador()