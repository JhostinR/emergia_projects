import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class Palabras:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Juego de Contador Palabras")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,400,600)
        # endregion configuracion de la ventana

        # region metodos
        # Funcion que cuenta las palabras
        def pedirTexto():
            self.texto = text_entry.get()
            self.numPalabras = len(self.texto.split())
            frase()

        # Funcion que muestra el resultado
        def frase():
            if not self.texto:
                result_label.config(text="Escribe una palabra o frase")
            else:
                result_label.config(text=f"El texto tiene {self.numPalabras} palabras.")
                button_salir.config(state=tk.NORMAL)
                count_button.config(state=tk.DISABLED)

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
        titulo_label = tk.Label(frame1, text="★ Juego de Contar Palabras ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        
        # Se posiciona el titulo
        titulo_label.place(x=0, y=30)

        # Se pone la imagen al frame
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        nueva_imagen = imgJuegos.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        # Se posiciona la imagen
        label = tk.Label(frame1)
        label.place(x=50, y=60)
        label.config(image=imagen_tk, bg="#ff9e18")
        
        # endregion Frame1
        
        # region Frame2
        
        # Se crea el frame 2
        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        
        # Se posiciona el frame
        frame2.place(x=300, y=80, width=300, height=420)

        # Se pone el texto "escribe una frase"
        mensaje_label = tk.Label(frame2, text="Escribe una frase", font=("Arial", 15, "bold"), foreground="#ff9e18", bg="#773dbd")
        mensaje_label.place(x=65, y=30)

        text_entry = tk.Entry(frame2, width=40)# Se configura la entrada de la frase
        text_entry.place(x=30, y=90)# Posicionando la entrada de la frase
        
        # Creando boton para contar palabras
        count_button = tk.Button(frame2, text="Contar palabras", command=pedirTexto, state=tk.NORMAL, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18")
        count_button.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        count_button.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        count_button.place(x=90, y=140)
        
        # Label que muestra el resultado, se le pone un font y un background color
        result_label = tk.Label(frame2, foreground="#ff9e18",font=("Arial", 14, "bold"), bg="#773dbd")
        result_label.place(x=30, y=190)
        
        # Creando el boton cerrar que el comando envia a salir de la ventana
        button_salir = tk.Button(frame2, text="Cerrar", command=salir, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff")
        
        # Creando el efecto hover al boton salir
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        
        # Posicionando el boton salir
        button_salir.place(x=90, y=260)

        # endregion Frame2
        
        # Abre la ventana
        self.ventana.mainloop()