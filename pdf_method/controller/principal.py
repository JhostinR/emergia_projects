
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
from tkinter import ttk
import PyPDF2
from util.Helpers import Helpers

help = Helpers() # inicializando los helpers

global mensaje_mostrado
mensaje_mostrado = True

class Visualizador:
    def __init__(self):

# Crea una ventana de Tkinter
        ventana = tk.Tk()
        ventana.title('Dividir PDF')
        ventana.config(bg='#ffd6dc')
        ventana.configure(width=500, height=300)# configura tamaño y altura de la ventana
        help.centerWindows(ventana,300,500) # height width
        
# LLamando el titulo
        titulo = tk.Label(ventana, text="Dιʋιԃιɾ PDF", font=("Arial", 20, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=170,y=8)
        
# Llamando el icono de la ventana
        logo = help.getImage("IconPrincipal", (200, 200))
        ventana.iconphoto(True, logo)
        
# Crea un cuadro de entrada para el nombre del archivo PDF
        entry_filename = tk.Entry(ventana, width=24)
        entry_filename.place(x=175,y=60)

# Crea un botón para seleccionar el archivo PDF
        button_select_file = tk.Button(ventana, text="𝙎𝙚𝙡𝙚𝙘𝙘𝙞𝙤𝙣𝙖𝙧 𝙖𝙧𝙘𝙝𝙞𝙫𝙤", command=lambda: select_file(entry_filename), width=18, bg='#ff8a9a')
        button_select_file.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_select_file.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_select_file.place(x=180,y=120)

# Crea un cuadro de entrada para el número de páginas por PDF
        entry_pages_per_pdf = tk.Entry(ventana, width=24)
        entry_pages_per_pdf.place(x=175,y=180)
        
# Dando una instruccion
        mensaje = tk.Label(ventana, text="Cuantas paginas quieres dividir", font=("Arial", 12, "bold"), foreground="#f7072b", bg="#ffd6dc")
        mensaje.place(x=130, y=205)

# Crea un botón para dividir el archivo PDF
        button_split_pdf = tk.Button(ventana, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", command=lambda: split_pdf(entry_filename.get(), entry_pages_per_pdf.get()), width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=180,y=260)



    # Función para seleccionar el archivo PDF
        def select_file(entry):
            # Abre un cuadro de diálogo para seleccionar el archivo PDF
            filename = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
            # Asigna el nombre del archivo PDF al cuadro de entrada
            entry.delete(0, tk.END)
            entry.insert(0, filename)
    
    # Función para dividir el archivo PDF
        def split_pdf(filename, pages_per_pdf):
            # Crea un objeto PDFReader para el archivo PDF
            reader = PyPDF2.PdfReader(filename)
    
            # Obtiene el número total de páginas del archivo PDF
            total_pages = len(reader.pages)
    
            # Itera sobre el archivo PDF, dividiendo el archivo en PDF de páginas_per_pdf páginas cada uno
            for i in range(0, total_pages, int(pages_per_pdf)):
                # Crea un objeto PDFWriter para el archivo PDF de salida
                writer = PdfWriter()
    
                # Agrega las páginas del archivo PDF al archivo PDF de salida
                for page in reader.pages[i:min(i + int(pages_per_pdf), total_pages)]:
                    writer.add_page(page)
    
                # Escribe el archivo PDF de salida con el nombre editado
                with open("{}_copia.pdf".format(filename), "wb") as output_file:
                    writer.write(output_file)
                
                
                # Verifica si el mensaje ya se ha mostrado
                global mensaje_mostrado
                if mensaje_mostrado:
                    # Muestra el mensaje de alerta
                    tk.messagebox.showinfo("PDF dividido", "El proceso de división de PDF se ha completado correctamente.")
                    # Establece el estado del mensaje a False
                    mensaje_mostrado = False

        ventana.mainloop()
# Ejecuta el código
if __name__ == "__main__":
    Visualizador()