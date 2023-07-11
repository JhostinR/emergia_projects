# region librerias 
# importando librerias necesarias
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import re
from models.util.Helpers import Helpers
# endregion librerias 

# llamando los helpers
help = Helpers()

# creando una clase
class Correo:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana) # Creando la ventana 
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Extractor de Correos") # # Haciendole el titulo / nombre a la ventana
        self.ventana.geometry("800x450") # Redimencionando la ventana 
        self.ventana.configure(bg='#ff9e18') # Configurando el color de fondo de la ventana
        self.ventana.resizable(False, False) # Bloqueando la redimencion de la ventana 
        help.centerWindows(self.ventana,450,800) # Llamando el helper para centrar la ventana
        # endregion configuracion de la ventana

        # region metodos
        # Funcion que extrae los correos
        def extraer_correos():
            texto = self.entry_texto.get("1.0", tk.END).strip()
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", texto)
            resultado_texto = "Correos encontrados:\n" + "\n".join(emails)
            self.label_resultado.config(text=resultado_texto)
            self.button_salir.config(state=tk.NORMAL)
            self.button_extraer.config(state=tk.DISABLED)
        
        # Funcion que cierra la ventana 
        def salir():
            self.ventana.destroy()
        # endregion metodos
        
        # region frame superior
        frameHeader = tk.Frame(self.ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1,bg='#8a36d2')
        frameHeader.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)

        logoemergia = help.getImage("imagenNavBar", (380, 80)) # Llamando la imagen con el helper
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2") # Configurando el color de fondo de la imagen 
        label.place(x=0,y=0,relwidth=1, relheight=1) # Posicionando el label 
        # endregion frame superior
        
        # region Frame 1
        frame1 = tk.Frame(self.ventana, bg='#ff9e18') 
        frame1.place(x=0, y=80, width=400, height=620)
        
        titulo_label = tk.Label(frame1, text="★ Extractor de correos ★", font=("Arial", 16, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando el titulo
        titulo_label.place(x=60, y=20) # Posicionando el titulo 
        
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value")) # Llamando la imagen con el helper
        self.nueva_imagen = imgJuegos.resize((250, 250)) # Redimencionando la imagen 
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        self.label = tk.Label(frame1) # Creando el label para la imagen 
        self.label.place(x=60, y=80) # Posicionando el label 
        self.label.config(image=self.imagen_tk, bg="#ff9e18") # Configurando el color de fondo al label de la imagen 
        # endregion Frame1
        
        # region Frame2
        frame2 = tk.Frame(self.ventana, bg='#773dbd') # Creando el frame y configurando el color de fondo 
        frame2.place(x=400, y=80, width=400, height=420) # Posicionando el frame
        
        # Se configura el color de la letra y el fondo
        self.label_texto = tk.Label(frame2, text="Escribe un texto que contenga correo electrónico:", font=("Arial", 12, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando un label para un mensaje 
        self.label_texto.place(x=9, y=20)

        self.entry_texto = scrolledtext.ScrolledText(frame2, width=30, height=4) # Creando una entrada de texto 
        self.entry_texto.place(x=70, y=90) # Posicioando la entrada de texto 
        
        # Creando boton para contar palabras
        self.button_extraer = tk.Button(frame2, text="Extraer", command=extraer_correos, state=tk.NORMAL, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18") # Creando el boton 
        self.button_extraer.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.button_extraer.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        self.button_extraer.place(x=140, y=205)
        
        # Label que muestra el resultado, se le pone un font y un background color
        self.label_resultado = tk.Label(frame2, font=("Arial", 12, "bold"), foreground="#ff9e18", bg="#773dbd") # Creando un frame
        self.label_resultado.place(x=100, y=260) # Posicionando el label resultado 
        
        # Creando el boton cerrar 
        self.button_salir = tk.Button(frame2, text="Cerrar", command=salir, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff") # Creando el boton de cerrar
        
        # Creando el efecto hover al boton salir 
        self.button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        self.button_salir.place(x=140, y=330) # Posicionando el boton cerrar
        
        # endregion Frame2
        
        # inicializando la ventana
        self.ventana.mainloop()