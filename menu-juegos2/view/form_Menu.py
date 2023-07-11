# Importando librerias necesarias
import tkinter as tk
from view.form_Par_Impar import ParesImpares
from view.form_madLibs import Madlibs
from view.form_Acronimo import Acronimo
from view.form_Calculadora_Propinas import CalcularPropina
from view.form_Contador_Palabras import Palabras
from view.form_Informacion_Biografia import Biografia
from view.form_Piedra_Papel_Tijera import Piedrapapeltijera
from view.form_Palindromo import Palindromo
from view.form_Extractor_Correos import Correo
from view.form_Adivina_Numero import AdivinarNumero
from view.form_Generador_Letras import Generador
from view.form_Salir import Salir
from models.util.Helpers import Helpers
from PIL import Image, ImageTk

help = Helpers()


# Creando una clase principal
class Menu:
    def __init__(self, datos_jugador=None):
        super().__init__()
# region recibir datos
        self.datos_jugador = datos_jugador
        self.contador = 0
# endregion recibir datos

# region configuracion ventana
        self.ventana = tk.Tk()
        self.ventana.title("Ventana menu")
        self.ventana.configure(width=1024, height=640)
        self.ventana['bg'] = '#bfabf7'
        help.centerWindows(self.ventana,640,1024)
        self.ventana.resizable(False, False)
# endregion configuracion ventana

    # region Frame superior
        
        frame_superior = tk.Frame(self.ventana, bg="#8a36d2")
        frame_superior.place(x=0, y=0, width=1024, height=85)

        imagen_superior = Image.open(help.leerConfig("imagenNavBar", "Value"))
        imagen_superior = imagen_superior.resize((520, 85), Image.LANCZOS)
        imagen_superior_tk = ImageTk.PhotoImage(imagen_superior)

        imagen_superior_label = tk.Label(frame_superior, image=imagen_superior_tk, bg="#8a36d2")
        imagen_superior_label.image = imagen_superior_tk
        imagen_superior_label.place(x=260, y=0)
        
    # endregion Frame superior
    
    # region frame 1
        
        frame1 = tk.Frame(self.ventana, bg='#ff9e18')
        frame1.place(x=0, y=80, width=512, height=620)

        self.imagen = Image.open(help.leerConfig("imagenJuegos", "Value"))
        self.nueva_imagen = self.imagen.resize((200, 200))
        self.imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)

        self.label = tk.Label(frame1)
        self.label.place(x=140, y=330)
        self.label.config(image=self.imagen_tk, bg="#ff9e18")

    # region titulo datos
        self.titulo_datos_label = tk.Label(frame1, text="ミ★ DATOS ★彡", font=("Arial", 20), foreground="#773dbd", bg="#ff9e18")
        self.titulo_datos_label.place(x=140, y=20)
    # endregion titulo datos
    
    # region mostrar datos

        self.datos_player = tk.Label(frame1, font=("Helvetica", 13, "bold"), bg="#e0592a", foreground="#773dbd", width=40, height=6)
        self.datos_player.place(x=50, y=100)
        
        # if self.datos_jugador:
        #     datos_texto = ""
        #     for key, value in self.datos_jugador.items():
        #         datos_texto += f"{key}: {value}\n"
        #     self.datos_player.config(text=datos_texto)
            
    # endregion mostrar datos
    
    # region contador
        self.contador_label = tk.Label(frame1, text="Contador: 0", font=("Helvetica", 13, "bold"), bg="#ffffff", foreground="#e0592a", width=40)
        self.contador_label.place(x=50, y=220)
   # endregion contador

    # region ultimo juego 
        self.ultimo_juego_label = tk.Label(frame1, text="El último juego registrado es: Ninguno", font=("Helvetica", 13, "bold"), bg="#9A75FF", foreground="#000", width=40, height=2)
        self.ultimo_juego_label.place(x=50, y=240)
    # endregion ultimo juego 
        
    # endregion frame 1

        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        frame2.place(x=512, y=80, width=512, height=620)

    # region titulo juegos
        self.titulo_juegos_label = tk.Label(frame2, text="ミ★ ELIGE EL JUEGO ★彡", font=("Arial", 20), foreground="#ff9e18", bg="#773dbd")
        self.titulo_juegos_label.place(x=80, y=30)
    # endregion titulo juegos

# region botones
        self.boton1 = tk.Button(frame2, text="Par o impar", width=17, height=2, bg="#773dbd", foreground="#ff9e18", font=("Helvetica", 9, "bold"), command=self.iniciar_parimpar)
        self.boton1.place(x=30, y=120)
        # Se crea el efecto hover al boton
        self.boton1.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton1.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton2 = tk.Button(frame2, text="Mad libs", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_madlibs)
        self.boton2.place(x=190, y=120)
        self.boton2.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton2.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton3 = tk.Button(frame2,text="Contador de palabras", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_contador_palabras)
        self.boton3.place(x=350, y=120)
        self.boton3.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton3.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton4 = tk.Button(frame2, text="Biografia", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.Iniciar_biografia)
        self.boton4.place(x=30, y=200)
        self.boton4.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton4.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton5 = tk.Button(frame2, text="Acronimo", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command= self.iniciar_acronimo)
        self.boton5.place(x=190, y=200)
        self.boton5.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton5.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton6 = tk.Button(frame2, text="Piedra, Papel o Tijera", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_piedrapapeltijera)
        self.boton6.place(x=350, y=200)
        self.boton6.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton6.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton7 = tk.Button(frame2, text="Adivina el numero", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_adivinaNumero)
        self.boton7.place(x=30, y=280)
        self.boton7.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton7.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton8 = tk.Button(frame2, text="Palindromo", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_palindromo)
        self.boton8.place(x=190, y=280)
        self.boton8.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton8.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton9 = tk.Button(frame2, text="Calcular propina", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_calcularpropinas)
        self.boton9.place(x=350, y=280)
        self.boton9.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton9.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton10 = tk.Button(frame2, text="Extractor correos", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_extractorcorreos)
        self.boton10.place(x=110, y=360)
        self.boton10.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton10.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))

        self.boton11 = tk.Button(frame2, text="Generar letras", width=17, height=2, bg="#773dbd", foreground="#ff9e18",  font=("Helvetica", 9, "bold"), command=self.iniciar_generador)
        self.boton11.place(x=270, y=360)
        self.boton11.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        self.boton11.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        
        self.boton_salir = tk.Button(frame2, text="SALIR", bg="#FC8A4A", bd="3", relief="solid", width=8, height=1, font=("Helvetica", 12, "bold"), command=self.cerrar_ventana)
        self.boton_salir.place(x=380, y=480)
        self.boton_salir.bind('<Enter>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        self.boton_salir.bind('<Leave>', lambda e: e.widget.config(bg='#FC8A4A', foreground="#000"))
# endregion botones  #e0592a   

    # Funcion que cierra la ventana
    def cerrar_ventana(self):
        self.ventana.destroy()
        salir = Salir(self.ventana)
        salir.mainloop()
    # Funcion que crea el contador y suma cada vez que se ingresa a un juego
    def incrementar_contador(self):
        self.contador += 1
        self.contador_label.config(text=f"Contador: {self.contador}")
        
    # region inicializar juegos
    def iniciar_parimpar(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Par o impar")
        self.ventana_parImpar = ParesImpares(self.ventana)
        self.ventana_parImpar.ventana_parImpar.mainloop()

    def iniciar_madlibs(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: MadLibs")
        ventana_madlibs = Madlibs(self.ventana)
        ventana_madlibs.ventana.mainloop()

    def iniciar_contador_palabras(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Contador de palabras")
        contador_palabras = Palabras(self.ventana)
        contador_palabras.window.mainloop()

    def Iniciar_biografia(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Biografia")
        biografia = Biografia(self.ventana)
        biografia.ventana.mainloop()

    def iniciar_piedrapapeltijera(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Piedra, papel o tijera")
        piedrapapeltijera = Piedrapapeltijera(self.ventana)
        piedrapapeltijera.mainloop()

    def iniciar_acronimo(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Acronimo")
        acronimo = Acronimo(self.ventana)
        acronimo.window.mainloop()
    
    def iniciar_calcularpropinas(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Calcular Propinas")
        CalcularPropina(self.ventana)
    
    def iniciar_palindromo(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Palindromo")
        juego_palindromo = Palindromo(self.ventana)
        juego_palindromo.ventana.mainloop()
    
    def iniciar_extractorcorreos(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Extractor de correos")
        juego = Correo(self.ventana)
        juego.ejecutar_extractor_correos()
    
    def iniciar_adivinaNumero(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Adivinar numero")
        adivinar = AdivinarNumero(self.ventana)
        adivinar.ventana.mainloop()

    def iniciar_generador(self):
        self.incrementar_contador()
        self.ultimo_juego_label.config(text="El último juego registrado es: Generador de letras")
        generador = Generador(self.ventana)
        generador.mainloop()
    # endregion inicializar juegos
        
    # ventana.mainloop()
        
    # Metodo que inicializa el menu
        self.ventana.mainloop()

