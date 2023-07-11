import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class Madlibs:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
        
        super().__init__()
        
        # region configuracion de la ventana
        self.ventana.title("Juego de MadLibs")
        self.ventana.geometry("600x620")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,620,600)
        # endregion configuracion de la ventana

        # region metodos

        # Funcion donde obtiene los datos que se ingresan y se ordenan en la frase, para luego mostrarla
        def mostrar_frase():
            nombre = entry_nombre.get()
            edad = entry_edad.get()
            marca = entry_marca.get()
            peso = entry_peso.get()
            cilindraje = entry_cilindraje.get()
            color = entry_color.get()
            velocidad = entry_velocidad.get()

            if not nombre or not edad or not marca or not peso or not cilindraje or not color or not velocidad:
                label_resultado.config(text="Escribe todos los datos")
            else:
                resultado = f"Un día, {nombre} compró\n una motocicleta {color},\n a sus {edad} años pudo comprar\n un vehículo el cual necesitaba.\n La motocicleta es una {marca},\n su cilindraje es de {cilindraje}\n centímetros cúbicos, pesa\n solamente {peso} kg y su velocidad\n máxima es {velocidad} km/h."

            label_resultado.config(text=resultado)

            # Se configura el boton de salir para que se desbloquee
            button_salir.config(state=tk.NORMAL)

            # Se configura el boton de enviar para que se bloquee
            button_enviar.config(state=tk.DISABLED)
        
        # Funcion para cerrar la ventana
        def cerrar_ventana():
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
        frame1.place(x=0, y=80, width=300, height=620)

        # Se le incorpora el titulo a el frame
        titulo = tk.Label(frame1, text="★ Juego de MadLibs ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")

        # Se posiciona el titulo
        titulo.place(x=35, y=100)

        # Se pone la imagen al frame
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        nueva_imagen = imgJuegos.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        # Se posiciona la imagen
        label = tk.Label(frame1)
        label.place(x=50, y=170)
        label.config(image=imagen_tk, bg="#ff9e18")
        
        # endregion Frame1
        
        # region Frame2

        # Se crea el frame 2
        frame2 = tk.Frame(self.ventana, bg='#773dbd')

        # Se posiciona el frame
        frame2.place(x=300, y=80, width=300, height=620)

        # Se configura el label de nombre
        label_nombre = tk.Label(frame2, text="Ingrese su nombre:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_nombre.place(x=10, y=10)# Posicionando el label de nombre

        entry_nombre = tk.Entry(frame2)# Se configura la entrada del nombre
        entry_nombre.place(x=10, y=32)# Posicionando la entrada del nombre

        # Se configura el label de la edad
        label_edad = tk.Label(frame2, text="Ingrese su edad:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_edad.place(x=10, y=54)# Posicionando el label de la edad
        
        entry_edad = tk.Entry(frame2)# Se configura la entrada de la edad
        entry_edad.place(x=10, y=76)# Posicionando la entrada de la edad

        # Se configura el label de la marca de la moto
        label_marca = tk.Label(frame2, text="Ingrese la marca de su moto:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_marca.place(x=10, y=98)# Posicionando el label de la marca
        
        entry_marca = tk.Entry(frame2)# Se configura la entrada de la marca
        entry_marca.place(x=10, y=120)# Posicionando la entrada de la marca

        # Se configura el label del peso de la moto
        label_peso = tk.Label(frame2, text="Ingrese el peso de la moto en Kg:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_peso.place(x=10, y=142)# Posicionando el label del peso
        
        entry_peso = tk.Entry(frame2)# Se configura la entrada del peso
        entry_peso.place(x=10, y=164)# Posicionando la entrada del peso

        # Se configura el label del cilindraje de la moto
        label_cilindraje = tk.Label(frame2, text="Ingrese el cilindraje de la moto Cm3:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_cilindraje.place(x=10, y=186)# Posicionando el label del cilindraje
        
        entry_cilindraje = tk.Entry(frame2)# Se configura la entrada del cilindraje
        entry_cilindraje.place(x=10, y=208)# Posicionando la entrada del cilindraje

        # Se configura el label del color de la moto
        label_color = tk.Label(frame2, text="Ingrese el color de la moto:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_color.place(x=10, y=230)# Posicionando el label del color
        
        entry_color = tk.Entry(frame2)# Se configura la entrada del color
        entry_color.place(x=10, y=252)# Posicionando la entrada del color

        # Se configura el label de la velocidad de la moto
        label_velocidad = tk.Label(frame2, text="Ingresa la velocidad de la moto km/h:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_velocidad.place(x=10, y=274)# Posicionando el label de la velocidad
        
        entry_velocidad = tk.Entry(frame2)# Se configura la entrada de la velocidad
        entry_velocidad.place(x=10, y=296)# Posicionando la entrada de la velocidad

        # Se crea el boton enviar que toma el comando de la funcion mostrar clase
        button_enviar = tk.Button(frame2, text="ENVIAR", command=mostrar_frase, state=tk.NORMAL, width=15, font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_enviar.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_enviar.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_enviar.place(x=30, y=505)

        # Se configura el color de la letra y el fondo
        label_resultado = tk.Label(frame2, bg="#773dbd", foreground="#ff9e18", font=("Helvetica", 11, "bold"))
        label_resultado.place(x=30, y=325)

        # Se crea el boton para cerrar la ventana
        button_salir = tk.Button(frame2, text="CERRAR", command=cerrar_ventana, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff")
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        button_salir.place(x=150, y=505)
        
        # endregion Frame2
        
        # Abre la ventana
        self.ventana.mainloop()