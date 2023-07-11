# region librerias
# importando librerias necesarias
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers
# endregion librerias

# llamando los helpers
help = Helpers()

# creando una clase 
class CalcularPropina:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana) # Creando la ventana 
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Juego de Calcular Propinas") # Creando un titulo / nombrando la ventana 
        self.ventana.geometry("800x450") # Redimencionando la ventana 
        self.ventana.configure(bg='#ff9e18') # Configurando el color de fondo de la ventana 
        self.ventana.resizable(False, False) # Bloqueando la redimencion de la ventana 
        help.centerWindows(self.ventana,450,800) # Llamando el helper para centrar la ventana 
        # endregion configuracion de la ventana

        # region metodos
        
        # Funcion que calcula la propina
        def calcular_propina():
            valor = float(entry_valor.get())
            porcentaje = float(entry_porcentaje.get())
            total_propina = valor * (porcentaje / 100)
            resultado_texto = f"El valor total es {valor} y se le sumará {total_propina}"
            label_resultado.config(text=resultado_texto)
            button_salir.config(state=tk.NORMAL)
            button_calcular.config(state=tk.DISABLED)
        
        # Funcion que cierra la ventana
        def salir():
            self.ventana.destroy()
            
        # endregion metodos
        
        # region frame superior
        frameHeader = tk.Frame(self.ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1,bg='#8a36d2')
        frameHeader.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)

        logoemergia = help.getImage("imagenNavBar", (380, 80))
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2")
        label.place(x=0,y=0,relwidth=1, relheight=1)
        # endregion frame superior
        
        # region Frame 1
        frame1 = tk.Frame(self.ventana, bg='#ff9e18') # Creando el frame y configurando el color de fondo 
        frame1.place(x=0, y=80, width=400, height=420) # Posicioando el frame
        
        titulo = tk.Label(frame1, text="★ Juego de Calcular Propinas ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18") # Configurando el titulo 
        titulo.place(x=40, y=20) # Posicionando el titulo 
        
        # Importando la imagen de juegos
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value")) 
        self.nueva_imagen = imgJuegos.resize((200, 200))
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        # Creando el label para la imagen
        self.label = tk.Label(frame1)
        self.label.place(x=90, y=100) # Posicionando el label 
        self.label.config(image=self.imagen_tk, bg="#ff9e18")
        # endregion Frame1
        
        # region Frame2
        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        frame2.place(x=400, y=80, width=400, height=420)
        
        # Se configura el color de la letra y el fondo
        label_valor = tk.Label(frame2, text="Ingresa el valor total de la factura o monto: $", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_valor.place(x=50, y=40)
        
        # Posicionando el label de entrada
        entry_valor = tk.Entry(frame2)
        entry_valor.place(x=140, y=80)
        
        # Se configura el color de la letra y el fondo
        label_porcentaje = tk.Label(frame2, text="Ingrese el porcentaje de propina que quieres dar (%):", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_porcentaje.place(x=30, y=140)
        
        # Posicionando el label de entrada
        entry_porcentaje = tk.Entry(frame2)
        entry_porcentaje.place(x=140, y=180)
        
        # Se crea el boton calcular que toma el comando de la funcion calcular propina
        button_calcular = tk.Button(frame2, text="CALCULAR", command=calcular_propina, state=tk.NORMAL, width=15,  font=("Arial", 9, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_calcular.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_calcular.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_calcular.place(x=50, y=320)
        
        # Se configura el color de la letra y el fondo
        label_resultado = tk.Label(frame2, bg="#773dbd", foreground="#ff9e18", font=("Helvetica", 10, "bold"))
        label_resultado.place(x=40, y=240)
        
        # Se crea el boton cerrar que cierra la ventana 
        button_salir = tk.Button(frame2, text="CERRAR", command=salir, state=tk.DISABLED, width=15, font=("Arial", 9, "bold"), bg="#e0592a", foreground="#fff")
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        button_salir.place(x=240, y=320)
        
        # endregion Frame2
        
        # inicializando la ventana 
        self.ventana.mainloop()