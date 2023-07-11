# region librerias 
# importando librerias necesarias
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import string
from models.util.Helpers import Helpers
# endregion libtrerias 

# llamando los helpers
help = Helpers()

# creando una clase
class Generador:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana) # Creando la ventana 
        self.mensaje = ""
        self.rstr = ""
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Generador de Letras") # Creando el titulo / nombrando la ventana
        self.ventana.geometry("800x450") # Redimencionando la ventana 
        self.ventana.configure(bg='#ff9e18') # Configurando el color de fondo a la ventana 
        self.ventana.resizable(False, False) # Bloqueando la redimencion de la ventana 
        help.centerWindows(self.ventana,450,800) # Llamando el helper para centrar la ventana 
        # endregion configuracion de la ventana

        # region metodos

        # Creando una funcion que genera una letra al azar
        def generar_letra():
            self.rstr = random.choice(string.ascii_letters)
            self.resultado_label.config(text=self.rstr)
            self.button_salir.config(state=tk.NORMAL)
            self.generar_letra_button.config(state=tk.DISABLED)
        
        # Creando funcion que cierra la ventana
        def salir():
            self.ventana.destroy()
        # endregion metodos
        
        # region frame superior
        frameHeader = tk.Frame(self.ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1,bg='#8a36d2') # Creando el frame superior 
        frameHeader.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)

        logoemergia = help.getImage("imagenNavBar", (380, 80)) # Llamando la imagen con los helper
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2")
        label.place(x=0,y=0,relwidth=1, relheight=1)
        # endregion frame superior
        
        # region Frame 1
        frame1 = tk.Frame(self.ventana, bg='#ff9e18') # Configurando el color del frame 
        frame1.place(x=0, y=80, width=400, height=420) # Posicionando el frame 
        
        titulo = tk.Label(frame1, text="★ Generador de Letras ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando el titulo 
        titulo.place(x=70, y=20) # Posicionando el titulo 
        
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value")) # Llamando la imagen con los helper
        self.nueva_imagen = imgJuegos.resize((250, 250)) #  Redimencionando la imagen 
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        self.label = tk.Label(frame1) # Creando el label para la imagen 
        self.label.place(x=60, y=80) # Posicionando la imagen 
        self.label.config(image=self.imagen_tk, bg="#ff9e18") # Configurando el color de fondo del label 
        # endregion Frame1
        
        # region Frame2
        frame2 = tk.Frame(self.ventana, bg='#773dbd') # Configurando el color de fondo al frame 
        frame2.place(x=400, y=80, width=400, height=420) # Posicionando el frame 
        
        # Se configura el color de la letra y el fondo
        self.mensaje = tk.Label(frame2, text="OPRIME EL BOTON GENERAR LETRA", font=("Arial", 11, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando un label para un mensaje 
        self.mensaje.pack(pady=15)
        
        # Se crea un boton para generar una letra 
        self.generar_letra_button = tk.Button(frame2, text="GENERAR LETRA", command=generar_letra, state=tk.NORMAL, width=15, height=1, font=("Helvetica", 10, "bold"), bg="#773dbd", foreground="#ff9e18") # Creando un boton
        self.generar_letra_button.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.generar_letra_button.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        self.generar_letra_button.pack(pady=15)
        
        # Label que muestra el resultado, se le pone un font y un background color
        self.resultado_label = tk.Label(frame2, text="", bg="#773dbd", foreground="#ff9e18", font=("Helvetica", 40, "bold")) # Creando el label de resultado 
        self.resultado_label.place(x=180, y=160) # Posicionando el label de resultado 

        
        # Creando el boton cerrar
        self.button_salir = tk.Button(frame2, text="CERRAR", command=salir, state=tk.DISABLED, width=15, height=1, font=("Helvetica", 10, "bold"), bg="#e0592a", foreground="#fff") # Creando el boton de cerrar 
        self.button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        # Posicionando el boton salir
        self.button_salir.place(x=135, y=290) # Posicionando el boton de cerrar
        
        # endregion Frame2
        
        # inicializando la ventana
        self.ventana.mainloop()