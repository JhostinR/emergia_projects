import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class Acronimo:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
    
        super().__init__()
        
        # region configuracion de la ventana
        
        self.ventana.title("Juego del Acronimo")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,400,600)
        # endregion configuracion de la ventana

        # region metodos
        # Se crea una funcion que crea los acronimos
        def convertirAcronimo():
            frase = entry.get()
            palabras = frase.split()
            acr = ""
        
            if not frase:
                result.config(text="Escribe la frase")
            else:
                for palabra in palabras:
                    acr += palabra[0].upper()

                result.configure(text=acr)
                button_salir.config(state=tk.NORMAL)
                button_convert.config(state=tk.DISABLED)
    
        # Funcion salir 
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
        titulo_label = tk.Label(frame1, text="★ Juego de Acronimos ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        
        # Se posiciona el titulo
        titulo_label.place(x=20, y=30)

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

        # Label creando un subtitulo indicando una instruccion
        mensaje_label = tk.Label(frame2, text="Escribe una frase", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        mensaje_label.place(x=60, y=30)
        
        # Se redimenciona el lugar para escribir la frase
        entry = tk.Entry(frame2, width=40)
        entry.place(x=30, y=80)
        
        # Creando un boton convertir donde su comando a convertir acronimo
        button_convert = tk.Button(frame2, text="CONVERTIR", command=convertirAcronimo, state=tk.NORMAL, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_convert.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_convert.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_convert.place(x=90, y=120)
        
        # Label que muestra el resultado, se le pone un font y un background color
        result = tk.Label(frame2, text="", foreground="#ff9e18",font=("Arial", 14, "bold"), bg="#773dbd")
        result.place(x=120, y=190)
        
        # Creando el boton cerrar que el comando envia a salir de la ventana 
        button_salir = tk.Button(frame2, text="CERRAR", command=salir, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff")
        
        # Creando el efecto hover para el boton cerrar
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        
        #posicionando el boton salir 
        button_salir.place(x=90, y=260)
        
        # endregion Frame2
        
        # Abre la ventana
        self.ventana.mainloop()