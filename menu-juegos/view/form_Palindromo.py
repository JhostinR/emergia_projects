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
class Palindromo:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana) # Creando la ventana
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Verificador de Palíndromos") # Creando un titulo / nombrando la ventana
        self.ventana.geometry("800x450") # Redimencionando la ventana
        self.ventana.configure(bg='#ff9e18') # Configurando color de fondo a la ventana
        self.ventana.resizable(False, False) # Bloquear la redimencion de la ventana
        help.centerWindows(self.ventana,450,800) # Llamando el helper para centrar la ventana
        # endregion configuracion de la ventana

        # region metodos
        # Funcion que verifica si es un palindromo o no
        def verificar_palindromo():
            texto = self.entry_texto.get()
            texto_sin_espacios = texto.replace(' ', '')
            texto_invertido = texto_sin_espacios[::-1]
            if not texto:
                self.label_resultado.config(text="Escribe una palabra o frase")
                self.label_resultado.place(x=90, y=210)
            else:
                if texto_sin_espacios.lower() == texto_invertido.lower():
                    resultado_texto = "La palabra es un palíndromo"
                else:
                    resultado_texto = "La palabra no es un palíndromo"
                self.label_resultado.config(text=resultado_texto)
                self.button_salir.config(state=tk.NORMAL)
                self.button_verificar.config(state=tk.DISABLED)
        # Funcion para cerrar la ventana
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
        frame1 = tk.Frame(self.ventana, bg='#ff9e18')
        frame1.place(x=0, y=80, width=400, height=420)
        
        titulo = tk.Label(frame1, text="★ Juego de Palindromos ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        titulo.place(x=50, y=20)
        
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        self.nueva_imagen = imgJuegos.resize((200, 200))
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        self.label = tk.Label(frame1)
        self.label.place(x=90, y=100)
        self.label.config(image=self.imagen_tk, bg="#ff9e18")
        # endregion Frame1
        
        # region Frame2
        frame2 = tk.Frame(self.ventana, bg='#773dbd') # Creanbdo el segundo frame y configurando el color de fondo
        frame2.place(x=400, y=80, width=400, height=420) # Posicionando el frame
        
        # Label creando un subtitulo indicando una instruccion
        self.mensaje_label = tk.Label(frame2, text="Escribe una frase o palabra para verificar si es palindromo", font=("Arial", 10, "bold"), foreground="#773dbd", bg="#ff9e18")
        self.mensaje_label.pack(pady=10) 

        # Se crea el lugar para escribir la frase
        self.entry_texto = tk.Entry(frame2, width=40) # Creando una entrada de texto
        self.entry_texto.place(x=80, y=80) # Posicioando la entrada de texto 

        # Se crea el boton para verificar si es palindromo o no
        self.button_verificar = tk.Button(frame2, text="VERIFICAR", command=verificar_palindromo, state=tk.NORMAL, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18") # Creando el boton de verificar
        self.button_verificar.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.button_verificar.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        self.button_verificar.place(x=145, y=150) # Posicopnando el boton 

        # Label que muestra el resultado, se le pone un font y un background color
        self.label_resultado = tk.Label(frame2, foreground="#ff9e18",font=("Arial", 12, "bold"), bg="#773dbd") # Creando un label que muestre el resultado
        self.label_resultado.place(x=85, y=210) # Posicionando el resultado

        # Creando el boton cerrar que el comando envia a salir de la ventana
        self.button_salir = tk.Button(frame2, text="CERRAR", command=salir, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff") # Creando el boton de cerrar ventana 
        # Posicionando el boton salir
        self.button_salir.place(x=140, y=280) # Posicinando el boton de cerrar 
        # Creando el efecto hover al boton salir
        self.button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        self.button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        
        # endregion Frame2
        
        # inicializando la ventana
        self.ventana.mainloop()