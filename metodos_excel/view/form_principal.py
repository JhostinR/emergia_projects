import tkinter as tk
from tkinter import filedialog, messagebox
from util.helpers import Helpers
from PIL import Image, ImageTk
import pandas as pd
from os import path, listdir, rename

help = Helpers()


class Visualizador:
    def __init__(self):
        # Crear una ventana_principal de Tkinter
        
        self.rutaPrincipalBusqueda = ''
        self.rutaPrincipalGuardado = ''
        self.missing_folders = []
        self.missing_files = []
        
        self.ventana_principal = tk.Tk()
        super().__init__()
        self.ventana_principal.title('Dividir PDF')
        self.ventana_principal.config(bg='#cafcd4')
        self.ventana_principal.geometry("600x550")  # Especificar el tamaño de la ventana_principal
        self.ventana_principal.resizable(False, False)
        help.centerWindows(self.ventana_principal, 550, 600)  # height width

        # Llama el icono de la ventana_principal
        logo = help.getImage("imagenExcel", (200, 200))
        self.ventana_principal.iconphoto(True, logo)

        imagen = Image.open(help.leerConfig("imagenPrincipal", "Value"))
        nueva_imagen = imagen.resize((300, 300))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        label = tk.Label(self.ventana_principal)
        label.place(x=150, y=100)
        label.config(image=imagen_tk, bg="#cafcd4")

        # Titulo principal
        titulo = tk.Label(self.ventana_principal, text="CONFIG EXCEL", font=("Arial", 26, "bold"), foreground="#016615", bg="#cafcd4")
        titulo.place(x=170, y=8)

        self.entry_filename = tk.Entry(self.ventana_principal, width=24)
        self.entry_filename.place_forget()

        self.select_file_button = tk.Button(self.ventana_principal, text="Seleccionar archivo", font=("Arial", 10, "bold"), command=self.select_file, width=18, bg='#b1fac0')
        self.select_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_file_button.place(x=220, y=70)

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
        self.select_folder_button.place(x=220, y=190)
        
        self.select_save_button = tk.Button(self.ventana_principal, text="Seleccionar carpeta guardado", font=("Arial", 10, "bold"), command=self.select_folder_save, width=24, bg='#b1fac0')
        self.select_save_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_save_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_save_button.place(x=200, y=290)
        
        self.selected_save_label = tk.Label(self.ventana_principal, text="Ruta Carpeta: ", font=("Arial", 8, "bold"), bg='#cafcd4')
        self.selected_save_label.place(x=20, y=340)

        self.entry_savefolder = tk.Entry(self.ventana_principal, width=24)
        self.entry_savefolder.place_forget()
        
        # Etiqueta para mostrar la ruta del archivo PDF seleccionado
        self.selected_folder_label = tk.Label(self.ventana_principal, text="Ruta del archivo: ", font=("Arial", 8, "bold"), bg='#cafcd4')
        self.selected_folder_label.place(x=20, y=240)

        self.select_folder_button = tk.Button(self.ventana_principal, text="Validar", font=("Arial", 10, "bold"), command=self.verify_files, width=18, bg='#b1fac0')
        self.select_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.select_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_folder_button.place(x=230, y=420)
        
        self.rename_file_button = tk.Button(self.ventana_principal, text="Renombrar archivo", font=("Arial", 10, "bold"), command=self.rename_file, width=18, bg='#b1fac0')
        self.rename_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.rename_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.rename_file_button.place(x=10, y=480)
        
        self.rename_folder_button = tk.Button(self.ventana_principal, text="Renombrar carpeta", font=("Arial", 10, "bold"), command=self.rename_folder, width=18, bg='#b1fac0')
        self.rename_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.rename_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.rename_folder_button.place(x=10, y=420)
        
        self.move_folder_button = tk.Button(self.ventana_principal, text="Mover Carpeta", font=("Arial", 10, "bold"), command=exit, width=18, bg='#b1fac0')
        self.move_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.move_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.move_folder_button.place(x=430, y=420)
        
        self.move_file_button = tk.Button(self.ventana_principal, text="Mover Archivo", font=("Arial", 10, "bold"), command=exit, width=18, bg='#b1fac0')
        self.move_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.move_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.move_file_button.place(x=430, y=480)

        # Botón salir
        self.exit_button = tk.Button(self.ventana_principal, text="Salir", font=("Arial", 10, "bold"), command=self.close, width=18, bg='#b1fac0')
        self.exit_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.exit_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.exit_button.place(x=230, y=500)
        
        self.ventana_principal.mainloop()

# ---------------------------------------------------------------------------------------------------------------------

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, file_path)

        if file_path:
            folder_name, file_name = path.split(file_path)
            parent_folder_name = path.basename(path.normpath(folder_name))  # Obtiene el nombre de la última carpeta

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

# ---------------------------------------------------------------------------------------------------------------------

    def select_folder(self):
            folder_path = filedialog.askdirectory()
            self.entry_foldername.delete(0, tk.END)
            self.entry_foldername.insert(0, folder_path)

            if folder_path:
                self.rutaPrincipalBusqueda = folder_path
                
                folder1, folder2 = path.split(folder_path)
                parent_folder_name = path.basename(path.normpath(folder1))

                self.selected_folder_label.config(text=f"Ruta del archivo: {parent_folder_name}/{folder2}")

# ---------------------------------------------------------------------------------------------------------------------

    def select_folder_save(self):
        folder_save_path = filedialog.askdirectory()
        self.entry_savefolder.delete(0, tk.END)
        self.entry_savefolder.insert(0, folder_save_path)

        if folder_save_path:
            self.rutaPrincipalGuardado = folder_save_path # Guardar la carpeta de destino seleccionada

            folder1, folder2 = path.split(folder_save_path)
            parent_folder_name = path.basename(path.normpath(folder1))

            self.selected_save_label.config(text=f"Ruta del archivo: {parent_folder_name}/{folder2}")

# ---------------------------------------------------------------------------------------------------------------------

    def validate_list_missing(self):
        if(len(self.missing_folders) > 0):
            dfFolders= pd.DataFrame.from_dict(self.missing_folders)
            dfFolders.to_excel("missing_folders.xlsx", index=False)

        if(len(self.missing_files) > 0):
            dfFiles = pd.DataFrame.from_dict(self.missing_files)
            dfFiles.to_excel("missing_files.xlsx", index=False)

# ---------------------------------------------------------------------------------------------------------------------

    def verify_files(self):
        file_path = self.entry_filename.get()
        folder_path = self.entry_foldername.get()
        
        if not path.exists(file_path):
            messagebox.showerror("Error", "El archivo seleccionado no existe.")
            return

        if not path.exists(folder_path):
            messagebox.showerror("Error", "La carpeta seleccionada no existe.")
            return

        if not file_path.endswith((".csv", ".xlsx")):
            messagebox.showerror("Error", "El archivo debe ser un archivo CSV o Excel.")
            return

        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, sep = ",")
        else:
            df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            folder_name = row.iloc[0]
            rutaCarpetaIndividual = path.exists(path.join(str(self.rutaPrincipalBusqueda), str(folder_name)))
            if(rutaCarpetaIndividual):
                file_names_in_folder = listdir(path.join(str(self.rutaPrincipalBusqueda), str(folder_name)))
                
                for col in row[1:]:
                    if col not in file_names_in_folder:
                        self.missing_files.append({"Archivo": f"{col}", "Carpeta contenedora": f"{folder_name}", "Estado": "No existe el archivo en la ruta"})
            else:
                self.missing_folders.append({"Carpeta": f"{folder_name}", "Estado": f"No existe la carpeta"})
                

        if self.validate_list_missing():
            messagebox.showinfo("Archivos faltantes", "se completo el proceso")
        else:
            messagebox.showinfo("Archivos coincidentes", "Se ha procesado")
            

# ---------------------------------------------------------------------------------------------------------------------

    def rename_file(self):
        file_path = self.entry_filename.get()
        
        if not file_path:
            messagebox.showerror("Error", "¡Selecciona un archivo!")
            return
        
        if not file_path.endswith((".csv", ".xlsx")):
            messagebox.showerror("Error", "El archivo debe ser un archivo CSV o Excel.")
            return
        
        # Leer el archivo Excel seleccionado
        df = pd.read_excel(file_path)
        
        # Eliminar filas que contienen valores NaN en alguna columna
        df = df.dropna(how='any')
        
        # Obtener la ruta de la carpeta que contiene el archivo Excel
        excel_folder = path.dirname(file_path)
        
        # Iterar a través de las filas del DataFrame
        for index, row in df.iterrows():
            folder_name = str(int(row['CARPETA']))
            current_file_name = row['NOMBRE ACTUAL']
            new_file_name = row['NUEVO NOMBRE']
        
            folder_path = path.join(str(excel_folder), str(folder_name))
            current_file_path = path.join(str(folder_path), str(current_file_name))
            new_file_path = path.join(self.rutaPrincipalGuardado, str(new_file_name))
        
            try:
                rename(current_file_path, new_file_path)
                messagebox.showinfo("¡Éxito!", f"El archivo '{current_file_name}' se ha guardado en la carpeta '{self.rutaPrincipalGuardado}' con el nuevo nombre '{new_file_name}'.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo '{current_file_name}' en la carpeta '{self.rutaPrincipalGuardado}': {str(e)}")

        messagebox.showinfo("¡Éxito!", "Se han renombrado y guardado los archivos según el archivo Excel en la carpeta de destino seleccionada.")

# ---------------------------------------------------------------------------------------------------------------------

    def rename_folder(self):
        file_path = self.entry_filename.get()  # Obtener la ruta del archivo Excel

        if not file_path:
            messagebox.showerror("Error", "¡Selecciona un archivo Excel!")
            return

        if not file_path.endswith((".xls", ".xlsx")):
            messagebox.showerror("Error", "El archivo debe ser un archivo Excel.")
            return

        # Leer el archivo Excel seleccionado
        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo Excel: {str(e)}")
            return

        # Obtener la ruta de la carpeta que contiene el archivo Excel
        excel_folder = path.dirname(file_path)

        # Iterar a través de las filas del DataFrame
        for index, row in df.iterrows():
            current_folder_name = row['Nombre Actual']
            new_folder_name = row['Nuevo Nombe']

            current_folder_path = path.join(str(excel_folder), str(current_folder_name))
            new_folder_path = path.join(str(excel_folder), str(new_folder_name))

            if path.exists(current_folder_path):
                try:
                    rename(current_folder_path, new_folder_path)
                    messagebox.showinfo("¡Éxito!", f"Se cambió el nombre de la carpeta '{current_folder_name}' a '{new_folder_name}'.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo cambiar el nombre de la carpeta '{current_folder_name}': {str(e)}")
            else:
                messagebox.showwarning("Advertencia", f"La carpeta '{current_folder_name}' no existe.")

        messagebox.showinfo("¡Éxito!", "Se han renombrado las carpetas según el archivo Excel.")

# ---------------------------------------------------------------------------------------------------------------------

    def close(self):
        self.ventana_principal.destroy()
    
if __name__ == "__main__":
    Visualizador()

