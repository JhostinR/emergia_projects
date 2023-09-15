import tkinter as tk
from tkinter import filedialog, messagebox
from util.helpers import Helpers
from PIL import Image, ImageTk
import pandas as pd
import os
from os import path
import shutil

help = Helpers()


class Visualizador:
    def __init__(self):
        # Crear una ventana_principal de Tkinter
        
        self.rutaPrincipalBusqueda = ''
        
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

        self.select_file_button = tk.Button(self.ventana_principal, text="Seleccionar archivo", font=("Arial", 10, "bold"), command=self.select_file, width=18, bg='#b1fac0')
        self.select_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_file_button.place(x=180, y=70)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_file_label = tk.Label(self.ventana_principal, text="Ruta del archivo: ", font=("Arial", 8, "bold"), bg='#cafcd4')
        self.selected_file_label.place(x=20, y=110)

        self.label_rows = tk.Label(self.ventana_principal, text="numero de registros", font=("Arial", 10, "normal"), bg='#cafcd4')
        self.label_rows.place(x=20, y=150)
        
        self.entry_foldername = tk.Entry(self.ventana_principal, width=24)
        self.entry_foldername.place_forget()

        self.select_folder_button = tk.Button(self.ventana_principal, text="Seleccionar carpeta", font=("Arial", 10, "bold"), command=self.select_folder, width=18, bg='#b1fac0')
        self.select_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_folder_button.place(x=180, y=190)

        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_folder_label = tk.Label(self.ventana_principal, text="Ruta del archivo: ", font=("Arial", 8, "bold"), bg='#cafcd4')
        self.selected_folder_label.place(x=20, y=240)

        self.select_folder_button = tk.Button(self.ventana_principal, text="Validar", font=("Arial", 10, "bold"), command=self.verify_files, width=18, bg='#b1fac0')
        self.select_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_folder_button.place(x=180, y=290)
        

        # Botón salir
        self.exit_button = tk.Button(self.ventana_principal, text="Salir", font=("Arial", 10, "bold"), command=self.close, width=18, bg='#b1fac0')
        self.exit_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.exit_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.exit_button.place(x=180, y=350)
        
        self.ventana_principal.mainloop()
    
    def select_file(self):
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


    def select_folder(self):
            folder_path = filedialog.askdirectory()
            self.entry_foldername.delete(0, tk.END)
            self.entry_foldername.insert(0, folder_path)

            if folder_path:
                self.rutaPrincipalBusqueda = folder_path
                folder1, folder2 = os.path.split(folder_path)
                parent_folder_name = os.path.basename(os.path.normpath(folder1))

                self.selected_folder_label.config(text=f"Ruta del archivo: {parent_folder_name}/{folder2}")

    def verify_files(self):
        file_path = self.entry_filename.get()
        folder_path = self.entry_foldername.get()
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "El archivo seleccionado no existe.")
            return

        if not os.path.exists(folder_path):
            messagebox.showerror("Error", "La carpeta seleccionada no existe.")
            return

        if not file_path.endswith((".csv", ".xlsx")):
            messagebox.showerror("Error", "El archivo debe ser un archivo CSV o Excel.")
            return

        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, sep = ",")
        else:
            df = pd.read_excel(file_path)
        
        missing_folders = []
        missing_files = []




        for index, row in df.iterrows():
            folder_name = row["0"]
            file_names_in_folder = os.listdir(path.join(str(self.rutaPrincipalBusqueda), str(folder_name)))
            
            if folder_name not in file_names_in_folder:
                missing_folders.append({"Carpeta": f"No existe carpeta: {folder_name}"})
            
            for col in row[1:]:
                if col not in file_names_in_folder:
                    missing_files.append({"Archivo": f"No existe archivo: {col}"})
        
        if missing_files:
            messagebox.showwarning("Archivos faltantes", f"Los siguientes archivos o carpetas no existen en la carpeta seleccionada:\n{''.join(str(missing_files))}")
        else:
            messagebox.showinfo("Archivos coincidentes", "Todos los archivos y carpetas existen en la carpeta seleccionada.")

    def close(self):
        self.ventana_principal.destroy()

if __name__ == "__main__":
    Visualizador()
