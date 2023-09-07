import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class Piedrapapeltijera:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
        
        super().__init__()
        
        # region configuracion de la ventana
        self.ventana.title("Juego de Piedra, Papel y Tijera")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,500,600)
        # endregion configuracion de la ventana

        # region metodos

        # Funcion para darle funcionalidad a los botones
        def jugar(seleccion):
            opciones = ["piedra", "papel", "tijera"]
            pc = random.choice(opciones)
            resultado = obtener_resultado(seleccion, pc)

            resultado_texto = f"Tú elegiste {seleccion}.\n La computadora eligió {pc}.\n Resultado: {resultado}"
            label_resultado.config(text=resultado_texto)

            # Se configura el boton de salir para que se desbloquee
            button_salir.config(state=tk.NORMAL)
        
            # Se configura el boton de piedra para que se bloquee
            button_piedra.config(state=tk.DISABLED)
        
            # Se configura el boton de papel para que se bloquee
            button_papel.config(state=tk.DISABLED)
        
            # Se configura el boton de tijera para que se bloquee
            button_tijera.config(state=tk.DISABLED)

        # Funcion para saber el resultado
        def obtener_resultado(usuario, pc):
            resultados = {
                "piedra": {"piedra": "empate", "papel": "perdiste", "tijera": "ganaste"},
                "papel": {"piedra": "ganaste", "papel": "empate", "tijera": "perdiste"},
                "tijera": {"piedra": "perdiste", "papel": "ganaste", "tijera": "empate"}
            }

            return resultados[usuario][pc]

        # Funcion para cerrar la ventana
        def salir():
            self.ventana.destroy()
        
        # endregion metodos
        
        # region frame superior
        
        # Se crea el frame superior
        frameHeader = tk.Frame(self.ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1,bg='#8a36d2')
        frameHeader.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)

        # Se incorpora la imagen a el frame superior
        logoemergia = help.getImage("imagenNavBar", (380, 80))
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2")
        
        # Se posiciona la imagen
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        # endregion frame superior
        
        # region Frame 1
        
        # Se crea el frame 1
        frame1 = tk.Frame(self.ventana, bg='#ff9e18')
        
        # Se posiciona el frame
        frame1.place(x=0, y=80, width=300, height=420)
        
        # Se le incorpora el titulo a el frame
        titulo = tk.Label(frame1, text="★ Juego de Piedra, papel, tijeras ★", font=("Arial", 13, "bold"), foreground="#773dbd", bg="#ff9e18")
        
        # Se posiciona el titulo
        titulo.place(x=5  , y=70)
        
        # Se pone la imagen al frame
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        nueva_imagen = imgJuegos.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        # Se posiciona la imagen
        label = tk.Label(frame1)
        label.place(x=50, y=130)
        label.config(image=imagen_tk, bg="#ff9e18")
        
        # endregion Frame1
        
        # region Frame2
        
        # Se crea el frame 2
        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        
        # Se posiciona el frame
        frame2.place(x=300, y=80, width=300, height=420)

        # Label creando un subtitulo indicando una instruccion
        mensaje_label = tk.Label(frame2, text="Escoge una opcion", font=("Arial", 12, "bold"), foreground="#ff9e18", bg="#773dbd")
        mensaje_label.pack(pady=10)

        # Se crea el boton para seleccionar piedra
        button_piedra = tk.Button(frame2, text="Piedra", command=lambda: jugar("piedra"), state=tk.NORMAL, width=17,  font=("Helvetica", 11, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_piedra.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_piedra.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_piedra.place(x=70, y=60)

        # Se crea el boton para seleccionar papel
        button_papel = tk.Button(frame2, text="Papel", command=lambda: jugar("papel"), state=tk.NORMAL, width=17,  font=("Helvetica", 11, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_papel.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_papel.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_papel.place(x=70, y=100)

        # Se crea el boton para seleccionar tijera
        button_tijera = tk.Button(frame2, text="Tijera", command=lambda: jugar("tijera"), state=tk.NORMAL, width=17,  font=("Helvetica", 11, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_tijera.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_tijera.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_tijera.place(x=70, y=140)

        # Label que muestra el resultado
        label_resultado = tk.Label(frame2, foreground="#ff9e18",font=("Arial", 12, "bold"), bg="#773dbd")
        label_resultado.place(x=40, y=220)

        # Creando el boton cerrar que el comando envia a salir de la ventana
        button_salir = tk.Button(frame2, text="CERRAR", command=salir, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff")
        
        # Posicionando el boton salir
        button_salir.place(x=95, y=330)
        
        # Creando el efecto hover al boton salir
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))

        # endregion Frame2
        
        # Abre la ventana
        self.ventana.mainloop()