import tkinter as tk
from tkinter import filedialog, messagebox
from util.helpers import Helpers
from PIL import Image, ImageTk
import pandas as pd
import shutil
from shutil import move
from os import path, listdir, rename, makedirs, walk

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
        self.select_folder_button.place(x=230, y=400)
        
        self.select_validar_button = tk.Button(self.ventana_principal, text="Validar 2.0", font=("Arial", 10, "bold"), command=self.validate_files_2, width=18, bg='#b1fac0')
        self.select_validar_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615')) 
        self.select_validar_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.select_validar_button.place(x=230, y=450)
        
        self.rename_file_button = tk.Button(self.ventana_principal, text="Renombrar archivo", font=("Arial", 10, "bold"), command=self.rename_file, width=18, bg='#b1fac0')
        self.rename_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.rename_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.rename_file_button.place(x=10, y=480)
        
        self.rename_folder_button = tk.Button(self.ventana_principal, text="Renombrar carpeta", font=("Arial", 10, "bold"), command=self.rename_folder, width=18, bg='#b1fac0')
        self.rename_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.rename_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.rename_folder_button.place(x=10, y=420)
        
        self.move_folder_button = tk.Button(self.ventana_principal, text="Mover Carpeta", font=("Arial", 10, "bold"), command=self.move_folders, width=18, bg='#b1fac0')
        self.move_folder_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.move_folder_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.move_folder_button.place(x=430, y=420)
        
        self.move_file_button = tk.Button(self.ventana_principal, text="Mover Archivo", font=("Arial", 10, "bold"), command=self.move_files, width=18, bg='#b1fac0')
        self.move_file_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.move_file_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.move_file_button.place(x=430, y=480)

        # Botón salir
        self.exit_button = tk.Button(self.ventana_principal, text="Salir", font=("Arial", 10, "bold"), command=self.close, width=18, bg='#b1fac0')
        self.exit_button.bind('<Enter>', lambda e: e.widget.config(bg='#016615'))
        self.exit_button.bind('<Leave>', lambda e: e.widget.config(bg='#b1fac0'))
        self.exit_button.place(x=230, y=500)
        
        self.ventana_principal.mainloop()

# region metodos

# ---------------------------------------------------------------------------------------------------------------------
#region select file
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
#endregion select file
# ---------------------------------------------------------------------------------------------------------------------
#region select folder
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.entry_foldername.delete(0, tk.END)
        self.entry_foldername.insert(0, folder_path)

        if folder_path:
            self.rutaPrincipalBusqueda = folder_path
            
            folder1, folder2 = path.split(folder_path)
            parent_folder_name = path.basename(path.normpath(folder1))

            self.selected_folder_label.config(text=f"Ruta del archivo: {parent_folder_name}/{folder2}")
#endregion select folder
# ---------------------------------------------------------------------------------------------------------------------
#region select folder save
    def select_folder_save(self):
        folder_save_path = filedialog.askdirectory()
        self.entry_savefolder.delete(0, tk.END)
        self.entry_savefolder.insert(0, folder_save_path)
    
        if folder_save_path:
            self.rutaPrincipalGuardado = folder_save_path
    
            folder1, folder2 = path.split(folder_save_path)
            parent_folder_name = path.basename(path.normpath(folder1))
    
            self.selected_save_label.config(text=f"Ruta del archivo: {parent_folder_name}/{folder2}")
#endregion select folder save
# ---------------------------------------------------------------------------------------------------------------------
#region validate list
    def validate_list_missing(self):
        if(len(self.missing_folders) > 0):
            dfFolders= pd.DataFrame.from_dict(self.missing_folders)
            dfFolders.to_excel("missing_folders.xlsx", index=False)

        if(len(self.missing_files) > 0):
            dfFiles = pd.DataFrame.from_dict(self.missing_files)
            dfFiles.to_excel("missing_files.xlsx", index=False)
#endregion validate list
# ---------------------------------------------------------------------------------------------------------------------
#region verify files
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
#endregion validate files
#----------------------------------------------------------------------------------------------------------------------
#region validar 2.0
    def validate_files_2(self):
        # Obtener la ruta de la carpeta seleccionada
        selected_folder_path = self.entry_foldername.get()

        # Validar que la carpeta exista
        if not selected_folder_path:
            messagebox.showerror("Error", "¡Selecciona una carpeta!")
            return

        # Crear una lista para almacenar las carpetas y archivos
        carpetas_archivos = []

        # Iterar a través de las subcarpetas de la carpeta seleccionada
        for subfolder_path, _, filenames in walk(selected_folder_path):
            # Obtener el nombre de la carpeta
            folder_name = path.basename(subfolder_path)

            # Crear una lista de archivos que contiene la carpeta
            file_names = [f for f in filenames if path.isfile(path.join(subfolder_path, f))]

            # Agregar la carpeta y los archivos a la lista
            carpetas_archivos.append({
                "Carpeta": folder_name,
                "Archivos": ";".join(file_names)
            })

        # Guardar la lista de carpetas y archivos en un archivo CSV
        df_carpetas_archivos = pd.DataFrame.from_dict(carpetas_archivos)
        df_carpetas_archivos.to_csv(path.join(self.rutaPrincipalGuardado, "carpetas_archivos.csv"), index=False)

        messagebox.showinfo("¡Éxito!", "Se ha creado el archivo CSV con las carpetas y archivos.")
        
#endregion validar 2.0
# ---------------------------------------------------------------------------------------------------------------------
#region rename files
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

        # Crear una lista para almacenar las ubicaciones originales de los archivos con nuevos nombres
        new_file_locations = []

        # Iterar a través de las filas del DataFrame
        for index, row in df.iterrows():
            folder_name = str(int(row['CARPETA']))
            current_file_name = row['NOMBRE ACTUAL']
            new_file_name = row['NUEVO NOMBRE']

            folder_path = path.join(str(excel_folder), str(folder_name))
            current_file_path = path.join(str(folder_path), str(current_file_name))
            new_folder_path = path.join(self.rutaPrincipalGuardado, str(folder_name))  # Utilizar el nombre de la carpeta como nombre de la carpeta de destino
            new_file_path = path.join(new_folder_path, str(new_file_name))  # Crear la ruta completa del archivo en la carpeta de destino

            # Crear la carpeta de destino si no existe
            if not path.exists(new_folder_path):
                try:
                    makedirs(new_folder_path)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo crear la carpeta de destino '{new_folder_path}': {str(e)}")
                    continue

            # Copiar el archivo con el nuevo nombre a la carpeta de destino
            try:
                shutil.copy(current_file_path, new_file_path)
                new_file_locations.append(new_file_path)  # Registrar la ubicación del nuevo archivo
                messagebox.showinfo("¡Éxito!", f"El archivo '{current_file_name}' se ha guardado en la carpeta '{new_folder_path}' con el nuevo nombre '{new_file_name}'.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo '{current_file_name}' en la carpeta '{new_folder_path}': {str(e)}")

        # Mostrar un mensaje al usuario con las ubicaciones originales de los archivos con nuevos nombres
        if new_file_locations:
            original_locations_message = "\n".join(new_file_locations)
            messagebox.showinfo("Ubicaciones originales de los archivos con nuevos nombres", f"Las ubicaciones originales de los archivos con nuevos nombres son:\n{original_locations_message}")

        messagebox.showinfo("¡Éxito!", "Se han renombrado y guardado los archivos según el archivo Excel en la carpeta de destino seleccionada.")

#endregion rename files
# ---------------------------------------------------------------------------------------------------------------------
#region rename folder
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
            new_folder_name = row['Nuevo Nombre']

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
#endregion rename folder
# ---------------------------------------------------------------------------------------------------------------------
#region move files
    def move_files(self):
            file_path = self.entry_filename.get()

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

            # Iterar a través de las filas del DataFrame
            for index, row in df.iterrows():
                folder_name = str(row['CARPETA ACTUAL'])
                file_name = str(row['NOMBRE DE ARCHIVO A MOVER'])
                dest_folder_name = str(row['CARPETA NUEVA'])
                new_file_name = str(row['NUEVO NOMBRE ARCHIVO'])

                folder_path = path.join(self.rutaPrincipalBusqueda, folder_name)
                dest_folder_path = path.join(self.rutaPrincipalGuardado, dest_folder_name)
                source_file_path = path.join(folder_path, file_name)
                dest_file_path = path.join(dest_folder_path, new_file_name)

                # Verificar si la carpeta de destino existe, y si no, crearla
                if not path.exists(dest_folder_path):
                    try:
                        makedirs(dest_folder_path)
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo crear la carpeta de destino '{dest_folder_path}': {str(e)}")
                        continue
                    
                # Mover el archivo a la carpeta de destino con el nuevo nombre
                try:
                    move(source_file_path, dest_file_path)
                    messagebox.showinfo("¡Éxito!", f"El archivo '{file_name}' se ha movido a la carpeta '{dest_folder_name}' con el nuevo nombre '{new_file_name}'.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo mover el archivo '{file_name}': {str(e)}")

            messagebox.showinfo("¡Éxito!", "Se han movido los archivos según el archivo Excel en la carpeta de destino seleccionada.")
#endregion move files
# ---------------------------------------------------------------------------------------------------------------------
#region move folder
    def move_folders(self):
        excel_file_path = self.entry_filename.get()
        dest_folder_path = self.entry_savefolder.get()

        if not excel_file_path or not dest_folder_path:
            messagebox.showerror("Error", "Selecciona el archivo Excel y la carpeta de destino.")
            return

        if not excel_file_path.endswith(".xlsx"):
            messagebox.showerror("Error", "El archivo debe ser un archivo Excel (.xlsx).")
            return

        if not path.exists(excel_file_path):
            messagebox.showerror("Error", "El archivo Excel seleccionado no existe.")
            return

        if not path.exists(dest_folder_path):
            messagebox.showerror("Error", "La carpeta de destino seleccionada no existe.")
            return

        # Leer el archivo Excel y obtener la lista de carpetas a mover
        try:
            df = pd.read_excel(excel_file_path)
            folder_names = df['Carpeta a Mover'].tolist()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo Excel: {str(e)}")
            return

        # Mover las carpetas a la carpeta de destino
        for folder_name in folder_names:
            src_folder_path = path.join(self.rutaPrincipalBusqueda, str(folder_name))
            dest_folder_path = path.join(self.rutaPrincipalGuardado, str(folder_name))

            if path.exists(src_folder_path):
                try:
                    shutil.move(src_folder_path, dest_folder_path)
                    messagebox.showinfo("Éxito", f"La carpeta '{folder_name}' se ha movido a '{dest_folder_path}'.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo mover la carpeta '{folder_name}': {str(e)}")
            else:
                messagebox.showwarning("Advertencia", f"La carpeta '{folder_name}' no existe en la ubicación de origen.")
#endregion move folder
# ---------------------------------------------------------------------------------------------------------------------
#region close
    def close(self):
        self.ventana_principal.destroy()
#endregion close
#----------------------------------------------------------------------------------------------------------------------

# endregion metodos


if __name__ == "__main__":
    Visualizador()

