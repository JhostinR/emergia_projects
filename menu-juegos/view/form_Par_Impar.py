import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class ParesImpares:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
        
        super().__init__()
        
        # region configuracion de la ventana
        self.ventana.title("Juego de pares e impares")
        self.ventana.geometry("600x450")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,450,600)
        # endregion configuracion de la ventana

        # region metodos

        # Funcion donde toma el dato y rectifica si es par o no
        def paresImpares():
            try:
                numero = int(entry.get())
                if numero % 2 == 0:
                    resultado = "El número es par".format(numero)
                else:
                    resultado = "El número es impar".format(numero)
                label_resultado.config(text=resultado)

                # Configuracion para habilitar el boton salir y desabilitar el boton de calcular
                button_salir.config(state=tk.NORMAL)
                button_calcular.config(state=tk.DISABLED)

            except ValueError:
                self.label_resultado.config(text="Error: Ingrese un número válido")

        # Funcion para cerrar la ventana
        def cerrar_ventana():
            self.ventana.destroy()

        # Funcion para verificar si el parametro "char" es un dígito o no.
        def validar_entrada(char):
            return char.isdigit()

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
        titulo_label = tk.Label(frame1, text="★ Juego de Pares e Impares ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        
        # Se posiciona el titulo
        titulo_label.place(x=0, y=50)

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

        # Mensaje de "digita un numero"
        mensaje = tk.Label(frame2, text="Digita un número", font=("Arial", 12, "bold"), foreground="#ff9e18", bg="#773dbd")
        mensaje.place(x=75, y=50)

        # Label para escribir el numero
        validation = self.ventana.register(validar_entrada)
        entry = tk.Entry(frame2, validate="key", validatecommand=(validation, "%S"))
        entry.place(x=85, y=110)

        #Configuracion del boton calcular
        button_calcular = tk.Button(frame2, text="CALCULAR", command=paresImpares, state=tk.NORMAL, width=15, font=("Helvetica", 9, "bold"), bg="#773dbd", foreground="#ff9e18")

        #Cambia los colores si el cursor esta sobre el boton o no
        button_calcular.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_calcular.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_calcular.place(x=85, y=170)

        # Creando el label de resultado
        label_resultado = tk.Label(frame2, font=("Arial", 14, "bold"), foreground="#ff9e18", bg="#773dbd")
        label_resultado.place(x=60, y=230)

        #Creando el boton de salir
        button_salir = tk.Button(frame2, text="CERRAR", command=cerrar_ventana, state=tk.DISABLED, width=15, font=("Helvetica", 9, "bold"), bg="#e0592a", foreground="#fff")
        button_salir.place(x=85, y=300)

        #Cambia los colores si el cursor esta sobre el boton o no
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))

        # endregion Frame2

        # abre la ventana
        self.ventana.mainloop()