# region librerias
# importando librerias necesarias
import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
from models.util.Helpers import Helpers
# endregion librerias

# llamando los helpers
help = Helpers()

# creando una clase 
class AdivinarNumero:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana) # creacion de la ventana
        
        self.numSecreto = 0
        self.intento = 0
        self.intentos = 0
        self.boton_verificar = None
        
        super().__init__()
        
        # region configuracion de la ventana
        self.ventana.title("Adivinar el números") # Haciendole el titulo / nombre a la ventana
        self.ventana.geometry("800x450") # Redimencionando la ventana 
        self.ventana.configure(bg='#ff9e18') # Configurando el color de fondo de la ventana
        self.ventana.resizable(False, False) # Haciendo que la ventana no redimencione
        help.centerWindows(self.ventana,450,800) # Llamando el helper para centrar la ventana
        # endregion configuracion de la ventana

        # region metodos

        # Se crea una funcion para adivinar el numero
        def adivinar():
            self.numSecreto = random.randint(1, 20) # Generando un numero random del numero del 1 al 20
            etiqueta_mensaje.config(text="Adivina el numero del 1 al 20:") # Creando una etiqueta que muestre un mensaje 
            etiqueta_mensaje.place(x=100, y=10) # Posicionando la etiqueta que muestra un mensaje 
            etiqueta_subtitulo.config(text="") # Poner el texto en vacio 

            self.entrada_intento = tk.Entry(self.ventana) # configurando una entrada de texto, haciendo que aparezca en la ventana
            self.entrada_intento.place(x=530, y=250) # posicionando la entrada de texto

            self.boton_verificar = tk.Button(self.ventana, text="Verificar", command=verificar, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18") # Creando un boton
            self.boton_verificar.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd")) # Efecto hover que cuando el puntero este encima del boton aparezca ese color de fondo y de letra
            self.boton_verificar.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18")) # Efecto hover que cuando el puntero este fuera del boton aparezca ese color de fondo y de letra
            self.boton_verificar.place(x=535, y=290) # Posicionando el boton

            boton_adivinar.config(state=tk.DISABLED) # Haciendo que el boton este bloqueado 

        # Funcion que verifica el estado de la adivinanza
        def verificar():
            intento = self.entrada_intento.get()
            intento = int(intento)
            self.intentos += 1

            if intento < self.numSecreto:
                mensaje = "El número secreto es mayor. ¡Sigue intentándolo!"
            elif intento > self.numSecreto:
                mensaje = "El número secreto es menor. ¡Sigue intentándolo!"
            else:
                mensaje = f"¡Felicidades! Adivinaste el número secreto en {self.intentos} intentos."
                self.boton_verificar.config(state=tk.DISABLED)  # Deshabilitar el botón "Verificar"
                button_salir.config(state=tk.NORMAL) # Habilitar el botón "CERRAR"
                boton_adivinar.config(state=tk.DISABLED)

            etiqueta_subtitulo.config(text=mensaje, fg="#F7F1F1")
            etiqueta_subtitulo.place(x=5, y=100)
            self.entrada_intento.delete(0, tk.END)

        # Se crea una instancia que cierra la ventana
        def cerrar_ventana():
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
        frame1 = tk.Frame(self.ventana, bg='#ff9e18') # Creando un frame y configurando el background color de ese frame
        frame1.place(x=0, y=80, width=400, height=420) # Posicionando el frame en la ventana
        
        titulo = tk.Label(frame1, text="★ Juego de Adivinar Numero ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando el titulo 
        titulo.place(x=50, y=20) #  Posicioando el titulo
        
        # Importando la imagen desde los helpers
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        self.nueva_imagen = imgJuegos.resize((200, 200))
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        # Creando el label para la imagen de juegos
        self.label = tk.Label(frame1)
        self.label.place(x=100, y=100)
        self.label.config(image=self.imagen_tk, bg="#ff9e18")
        # endregion Frame1
        
        # region Frame2
        # Frame para el resto de los elementos
        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        frame2.place(x=400, y=80, width=400, height=420)

        # Label creando un subtitulo indicando una instruccion
        etiqueta_mensaje = tk.Label(frame2, text="Presiona 'Adivinar' para empezar el juego.", font=("Arial", 10, "bold"), foreground="#773dbd", bg="#ff9e18") # Creando una etiqueta mensaje 
        etiqueta_mensaje.place(x=60, y=20) # Posicioando la etiqueta
        
        # Creando un boton adivinar numero
        boton_adivinar = tk.Button(frame2, text="ADIVINAR NUMERO", command=adivinar, state=tk.NORMAL, width=15,  font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18") # Creando el boton 
        boton_adivinar.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        boton_adivinar.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        boton_adivinar.place(x=20, y=290) # Posicionando el boton 

        # Se le pone nun tipo de letra diferente al resultado que salga
        etiqueta_subtitulo = tk.Label(frame2, text="", font=("Arial", 12), bg="#773dbd") # Creando una etiqueta para que se mueste el resultado
        etiqueta_subtitulo.place(x=20, y=50) # Posicionando la etiqueta
        
        # Creando el boton cerrar que el comando envia a salir de la ventana 
        button_salir = tk.Button(frame2, text="CERRAR", command=cerrar_ventana, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff") # Creando el boton de cerrar 
        button_salir.place(x=270, y=290) # Posicionando el boton cerrar
        
        # Creando el efecto hover para el boton cerrar
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000")) # Efecto hover que cuando el puntero del mouse este sobre el boton se muestre ese color de fondo y de letra
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff")) # Efecto hover que cuando el puntero del mouse este fuera del boton se muestre ese color de fondo y de letra
        # endregion Frame2
        
        # inicializando la ventana
        self.ventana.mainloop()