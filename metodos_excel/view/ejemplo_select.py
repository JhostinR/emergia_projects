import tkinter as tk
from tkinter import filedialog
from util.helpers import Helpers
from PIL import Image, ImageTk
import pandas as pd
import os
import shutil

help = Helpers()


class Visualizador:
    def __init__(self):
        # Crear una ventana_principal de Tkinter
        self.ventana_principal = tk.Tk()
        super().__init__()
        self.ventana_principal.title('Dividir PDF')
        self.ventana_principal.config(bg='#cafcd4')
        self.ventana_principal.configure(width=500, height=400)  # configura tamaño y altura de la ventana_principal
        self.ventana_principal.geometry("500x400")  # Especificar el tamaño de la ventana_principal
        self.ventana_principal.resizable(False, False)
        help.centerWindows(self.ventana_principal, 400, 500)  # height width

        # Llama el icono de la ventana_principal
        logo = help.getImage("imagenExcel", (200, 200))
        self.ventana_principal.iconphoto(True, logo)

        imagen = Image.open(help.leerConfig("imagenPrincipal", "Value"))
        nueva_imagen = imagen.resize((280, 280))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        label = tk.Label(self.ventana_principal)
        label.place(x=120, y=80)
        label.config(image=imagen_tk, bg="#cafcd4")

        # Titulo principal
        titulo = tk.Label(self.ventana_principal, text="CONFIG EXCEL", font=("Arial", 26, "bold"), foreground="#016615", bg="#cafcd4")
        titulo.place(x=120, y=8)

        self.entry_filename = tk.Entry(self.ventana_principal, width=24)
        self.entry_filename.place_forget()

        self.select_file_button = tk.Button(self.ventana_principal, text="Seleccionar archivo", font=("Arial", 10, "bold"), command=self.select_pdf_file, width=18, bg='#b1fac0')
        self.select_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_file_button.place(x=180, y=70)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_file_label = tk.Label(self.ventana_principal, text="Ruta del archivo: ", font=("Arial", 8, "bold"), bg='#cafcd4')
        self.selected_file_label.place(x=20, y=110)

        self.label_rows = tk.Label(self.ventana_principal, text="numero de registros", font=("Arial", 10, "normal"), bg='#cafcd4')
        self.label_rows.place(x=20, y=150)

        # Menú desplegable
        self.option_var = tk.StringVar(self.ventana_principal)
        self.option_var.set("Seleccionar opción")  # Valor predeterminado
        options = ["Seleccionar opción", "Mover", "Renombrar", "Copiar"]
        option_menu = tk.OptionMenu(self.ventana_principal, self.option_var, *options)
        option_menu.config(width=20, font=("Arial", 10, "bold"), bg='#b1fac0')
        option_menu.place(x=180, y=250)

        # Botón Aceptar
        self.accept_button = tk.Button(self.ventana_principal, text="Aceptar", font=("Arial", 10, "bold"), command=self.process_action, width=18, bg='#b1fac0')
        self.accept_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.accept_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.accept_button.place(x=180, y=300)

        # Botón salir
        self.exit_button = tk.Button(self.ventana_principal, text="salir", font=("Arial", 10, "bold"), command=self.close, width=18, bg='#b1fac0')
        self.exit_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.exit_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.exit_button.place(x=180, y=350)
        
        self.ventana_principal.mainloop()

    def close(self):
        self.ventana_principal.destroy()
    
    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, file_path)

        if file_path:
            folder_name, file_name = os.path.split(file_path)
            parent_folder_name = os.path.basename(os.path.normpath(folder_name))  # Obtiene el nombre de la última carpeta

            self.selected_file_label.config(text=f"Ruta del archivo: {parent_folder_name}/{file_name}")

            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
                num_rows = len(df.index)
                self.label_rows.config(text=f"Número de registros: {num_rows}")
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path)
                num_rows = len(df.index)
                self.label_rows.config(text=f"Número de registros: {num_rows}")
            else:
                df = pd.read_csv(file_path)
                num_rows = len(df.index)
                self.label_rows.config(text=f"Número de registros: {num_rows}")

    def process_action(self):
        selected_action = self.option_var.get()
        source_file_path = self.entry_filename.get()

        if selected_action == "Renombrar":
            new_name = filedialog.asksaveasfilename(defaultextension=os.path.splitext(source_file_path)[1])
            if new_name:
                # Copia el archivo original a la nueva ubicación y renómbralo
                shutil.copy(source_file_path, new_name)
                self.entry_filename.delete(0, tk.END)
                self.entry_filename.insert(0, new_name)
                self.selected_file_label.config(text=f"Ruta del archivo: {new_name}")

        elif selected_action == "Mover":
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                destination_path = os.path.join(destination_folder, os.path.basename(source_file_path))
                # Copia el archivo original a la nueva ubicación y renómbralo
                shutil.copy(source_file_path, destination_path)
                self.entry_filename.delete(0, tk.END)
                self.entry_filename.insert(0, destination_path)
                self.selected_file_label.config(text=f"Ruta del archivo: {destination_path}")

        elif selected_action == "Copiar":
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                destination_path = os.path.join(destination_folder, os.path.basename(source_file_path))
                # Copia el archivo original a la nueva ubicación y renómbralo
                shutil.copy(source_file_path, destination_path)
                self.entry_filename.delete(0, tk.END)
                self.entry_filename.insert(0, destination_path)
                self.selected_file_label.config(text=f"Ruta del archivo: {destination_path}")


if __name__ == "__main__":
    Visualizador()
