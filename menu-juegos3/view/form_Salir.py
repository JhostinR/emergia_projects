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
class Salir:
    def __init__(self,ventana):
        ventana = tk.Tk() # Creando la ventana
        
        super().__init__()
        # region configuracion de la ventana
        ventana.title("Game Over") # Creando un titulo / nombrando la ventana
        ventana.geometry("800x450") # Redimencionando la ventana
        ventana.configure(bg='#ff9e18') # Configurando color de fondo a la ventana
        ventana.resizable(False, False) # Bloquear la redimencion de la ventana
        help.centerWindows(ventana,450,800) # Llamando el helper para centrar la ventana
        # endregion configuracion de la ventana

        # region metodos
        # Funcion para cerrar la ventana
        def salir():
            ventana.destroy()
            
            # Funcion que crea el contador y suma cada vez que se ingresa a un juego
        def incrementar_contador(self):
            self.contador += 1
            contador_label.config(text=f"Contador: {self.contador}")
        
        # endregion metodos
        
        # region frame superior
        frameHeader = tk.Frame(ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1,bg='#8a36d2')
        frameHeader.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)

        logoemergia = help.getImage("imagenNavBar", (380, 80))
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2")
        label.place(x=0,y=0,relwidth=1, relheight=1)
        # endregion frame superior
        
        # region Frame 1
        frame1 = tk.Frame(ventana, bg='#ff9e18')
        frame1.place(x=0, y=80, width=300, height=420)
        
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        self.nueva_imagen = imgJuegos.resize((200, 200))
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        self.label = tk.Label(frame1)
        self.label.place(x=40, y=100)
        self.label.config(image=self.imagen_tk, bg="#ff9e18")
        
        titulo = tk.Label(frame1, text="ミ DATOS DEL JUGADOR 彡", font=("Helvetica", 16, "bold"), bg="#ff9e18", foreground="#773dbd")
        titulo.place(x=0, y=20)
        # endregion Frame1
        
        # region Frame2
        frame2 = tk.Frame(ventana, bg='#773dbd')
        frame2.place(x=300, y=80, width=700, height=420)
        
        datos_player = tk.Label(frame2, font=("Helvetica", 13, "bold"), bg="#e0592a", foreground="#773dbd", width=40, height=6)
        datos_player.place(x=50, y=60)
        
        # region contador
        contador_label = tk.Label(frame2, text="Contador: 0", font=("Helvetica", 13, "bold"), bg="#ffffff", foreground="#e0592a", width=40)
        contador_label.place(x=50, y=180)
        # endregion contador

        # region ultimo juego 
        ultimo_juego_label = tk.Label(frame2, text="El último juego registrado es: Ninguno", font=("Helvetica", 13, "bold"), bg="#9A75FF", foreground="#000", width=40, height=2)
        ultimo_juego_label.place(x=50, y=200)
        # endregion ultimo juego
        
        #Creando el boton de salir
        button_salir = tk.Button(frame2, text="CERRAR", command=salir, width=15, font=("Helvetica", 10, "bold"), bg="#e0592a", foreground="#fff")
        button_salir.place(x=200, y=300)

        #Cambia los colores si el cursor esta sobre el boton o no
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        
        # endregion Frame2
        
        # inicializando la ventana
        ventana.mainloop()