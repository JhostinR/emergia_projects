import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from models.util.Helpers import Helpers

help = Helpers()

class Biografia:
    def __init__(self,ventana):
        self.ventana = Toplevel(ventana)
        
        super().__init__()
        # region configuracion de la ventana
        self.ventana.title("Juego de Biografia")
        self.ventana.geometry("800x620")
        self.ventana.configure(bg='#ff9e18')
        self.ventana.resizable(False, False)
        help.centerWindows(self.ventana,620,800)
        # endregion configuracion de la ventana

        # region metodos
        # Funcion donde obtiene los datos que se ingresan y se ordenan en la frase, para luego mostrarla
        def mostrar_frase():
            nombre = entry_nombre.get()
            dia = entry_dia.get()
            mes = entry_mes.get()
            año = entry_año.get()
            profesion = entry_profesion.get()
            lugar_nacimiento = entry_lugar_nacimiento.get()
            lugar_estudio = entry_lugar_estudio.get()
            nombre_madre = entry_nombre_madre.get()
            nombre_padre = entry_nombre_padre.get()
            num_hermanos = entry_num_hermanos.get()

            if not nombre or not dia or not mes or not año or not profesion or not lugar_nacimiento or not lugar_estudio or not nombre_madre or not nombre_padre or not num_hermanos:
                label_resultado.config(text="Escribe todos los datos")
            else:
                frase = f"{nombre} nació el {dia} de {mes}\n del año {año}, en {lugar_nacimiento}.\n Es un/una {profesion} el cual\n se graduó en {lugar_estudio}. Su madre se llama\n {nombre_madre} y su padre {nombre_padre} y tiene\n en total {num_hermanos} hermano/s."

            label_resultado.config(text=frase)

            # Se configura el boton de salir para que se desbloquee
            button_salir.config(state=tk.NORMAL)

            # Se configura el boton de enviar para que se bloquee
            button_enviar.config(state=tk.DISABLED)

        # Instancia para cerrar la ventana
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
        frame1.place(x=0, y=80, width=400, height=620)

        # Se le incorpora el titulo a el frame
        titulo_label = tk.Label(frame1, text="★ Juego de Biografia ★", font=("Arial", 14, "bold"), foreground="#773dbd", bg="#ff9e18")
        
        # Se posiciona el titulo
        titulo_label.place(x=90, y=100)

        # Se pone la imagen al frame
        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        nueva_imagen = imgJuegos.resize((300, 300))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        # Se posiciona la imagen
        label = tk.Label(frame1)
        label.place(x=30, y=160)
        label.config(image=imagen_tk, bg="#ff9e18")
        
        # endregion Frame1
        
        # region Frame2
        
        # Se crea el frame 2
        frame2 = tk.Frame(self.ventana, bg='#773dbd')
        
        # Se posiciona el frame
        frame2.place(x=400, y=80, width=400, height=620)

        # Se configura el label de nombre
        label_nombre = tk.Label(frame2, text="Ingrese su nombre:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_nombre.place(x=10, y=40)

        # Posicionando el label de nombre
        entry_nombre = tk.Entry(frame2)
        entry_nombre.place(x=240, y=40)

        # Se configura el label del dia de nacimiento
        label_dia = tk.Label(frame2, text="Ingrese su día de nacimiento:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_dia.place(x=10, y=70)
        
        # Posicionando el label del dia de nacimiento
        entry_dia = tk.Entry(frame2)
        entry_dia.place(x=240, y=70)

        # Se configura el label del mes de nacimiento
        label_mes = tk.Label(frame2, text="Ingrese su mes de nacimiento:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_mes.place(x=10, y=100)

        # Posicionando el label del mes de nacimiento
        entry_mes = tk.Entry(frame2)
        entry_mes.place(x=240, y=100)

        # Se configura el label del año de nacimiento
        label_año = tk.Label(frame2, text="Ingrese su año de nacimiento:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_año.place(x=10, y=130)
        
        # Posicionando el label del año de nacimiento
        entry_año = tk.Entry(frame2)
        entry_año.place(x=240, y=130)

        # Se configura el label de la profesion 
        label_profesion = tk.Label(frame2, text="Cual es su profesión?", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_profesion.place(x=10, y=160)
        
        # Posicionando el label de la profesion 
        entry_profesion = tk.Entry(frame2)
        entry_profesion.place(x=240, y=160)

        # Se configura el label del lugar de nacimiento
        label_lugar_nacimiento = tk.Label(frame2, text="Ingrese su lugar de nacimiento:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_lugar_nacimiento.place(x=10, y=190)
        
        # Posicionando el label del lugar de nacimiento
        entry_lugar_nacimiento = tk.Entry(frame2)
        entry_lugar_nacimiento.place(x=240, y=190)

        # Se configura el label del lugar donde se graduo
        label_lugar_estudio = tk.Label(frame2, text="Ingrese el lugar donde se graduó:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_lugar_estudio.place(x=10, y=220)
        
        # Posicionando el label del lugar donde se graduo
        entry_lugar_estudio = tk.Entry(frame2)
        entry_lugar_estudio.place(x=240, y=220)

        # Se configura el label de la madre
        label_nombre_madre = tk.Label(frame2, text="Ingrese el nombre de su madre:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_nombre_madre.place(x=10, y=250)
        
        # Posicionando el label de la madre
        entry_nombre_madre = tk.Entry(frame2)
        entry_nombre_madre.place(x=240, y=250)

        # Se configura el label del padre
        label_nombre_padre = tk.Label(frame2, text="Ingrese el nombre de su padre:", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_nombre_padre.place(x=10, y=280)
        
        # Posicionando el label del padre
        entry_nombre_padre = tk.Entry(frame2)
        entry_nombre_padre.place(x=240, y=280)

        # Se configura el label de los hermanos que tiene
        label_num_hermanos = tk.Label(frame2, text="Cuantos hermanos tiene?", foreground="#ff9e18", bg="#773dbd",font=("Helvetica", 10, "bold"))
        label_num_hermanos.place(x=10, y=310)
        
        # Posicionando el label de los hermanos que tiene
        entry_num_hermanos = tk.Entry(frame2)
        entry_num_hermanos.place(x=240, y=310)

        # Se crea el boton enviar que toma el comando de la funcion mostrar clase
        button_enviar = tk.Button(frame2, text="ENVIAR", command=mostrar_frase, state=tk.NORMAL, width=15, font=("Helvetica", 10, "bold"), bg="#773dbd", foreground="#ff9e18")
        button_enviar.bind('<Enter>', lambda e: e.widget.config(bg='#ff9e18', foreground="#773dbd"))
        button_enviar.bind('<Leave>', lambda e: e.widget.config(bg='#773dbd', foreground="#ff9e18"))
        button_enviar.place(x=60, y=490)

        # Se configura el color de la letra y el fondo
        label_resultado = tk.Label(frame2, bg="#773dbd", foreground="#ff9e18", font=("Helvetica", 11, "bold"))
        label_resultado.place(x=20, y=350)

        # Se crea el boton para cerrar la ventana
        button_salir = tk.Button(frame2, text="CERRAR", command=cerrar_ventana, state=tk.DISABLED, width=15, font=("Helvetica", 10, "bold"), bg="#e0592a", foreground="#fff")
        button_salir.bind('<Enter>', lambda e: e.widget.config(bg='#bfabf7', foreground="#000"))
        button_salir.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        button_salir.place(x=230, y=490) # Posicionando el boton paraq cerrar la ventana

        # endregion Frame2
        
        # Abre la ventana
        self.ventana.mainloop()