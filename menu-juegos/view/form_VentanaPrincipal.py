# region importaciones necesarias
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk
from view.form_Menu import Menu
from view.form_Registro import Registro
from models.util.Helpers import Helpers
from controller.usuario import Usuario
# endregion importaciones necesarias

help = Helpers() # inicializando los helpers
usuario = Usuario()

class VentanaPrincipal(): # creando una clase
    def __init__(self):
        ventana = tk.Tk()  
        super().__init__()
        
        # region configuracion de la ventana
        ventana.title("Ventana Principal") # se configura el titulo principal
        ventana.configure(width=1024, height=640)# configura tamaño y altura de la ventana
        ventana.resizable(False, False) # hace que no se redimencione
        help.centerWindows(ventana,640,1024) # height width
        
        
        logo = help.getImage("IconPrincipal", (200, 200))
        ventana.iconphoto(True, logo)
        # endregion configuracion de la ventana
        
        # region metodos
        # abrir registro
        def abrir_registro():
            Registro(ventana, datos_label)
            
        # cerrar ventana
        def cerrar_ventana():
            ventana.destroy()
            
        # abrir menu
        def abrir_menu():
            cerrar_ventana()
            menu = Menu()
            menu.ventana.mainloop()
        
        # borrar registro
        def borrar_registro():
            usuario.borrarDatos()  # Llamar al método de Usuario para borrar los datos
            datos_label.config(text="")  # Actualizar el contenido de datos_label
        
            
        # actualizar datos del jugador
        
        def actualizar_datos_jugador(dataUsuario):
            print(dataUsuario)
            print("hola")
            
            mesaje = dataUsuario


                # helpers.SetInfoDisabled(txtLoadFolder,"0")
        # endregion metodos
        
        # region Frame superior
        frame_superior = tk.Frame(ventana, bg="#8a36d2")
        frame_superior.place(x=0, y=0, width=1024, height=640)

        imagen_superior = Image.open(help.leerConfig("imagenNavBar", "Value"))
        imagen_superior = imagen_superior.resize((380, 80), Image.LANCZOS)
        imagen_superior_tk = ImageTk.PhotoImage(imagen_superior)
        
        imagen_superior_label = tk.Label(frame_superior, image=imagen_superior_tk, bg="#8a36d2")
        imagen_superior_label.image = imagen_superior_tk  # Mantener una referencia para evitar que se elimine la imagen
        imagen_superior_label.place(x=330, y=0)
        # endregion Frame superior

        # region Frame 1
        frame1 = tk.Frame(ventana, bg="#c486fa")
        frame1.place(x=0, y=80, width=512, height=700)
        
        imagen = Image.open(help.leerConfig("iconInicio", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        label = tk.Label(frame1)
        label.place(x=120, y=50)
        label.config(image=imagen_tk, bg="#c486fa")
        
        datos_label = tk.Label(frame1, font=("Arial", 12), bg="#e0592a", foreground="white", text= "", width=30, height=5)
        datos_label.pack()
        datos_label.place(x=120, y=380)
        # endregion Frame 1

        # region Frame 2
        frame2 = tk.Frame(ventana, bg="#bfabf7")
        frame2.place(x=512, y=80, width=512, height=700)

        background_image = tk.PhotoImage(file=help.leerConfig("backgroundImage", "Value"))
        background_label = tk.Label(frame2, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        titulo_label = tk.Label(frame2, text="ミ★ MENU JUEGOS ★彡", font=("Arial", 25), foreground="#773dbd", bg="#bfabf7")
        titulo_label.place(x=50, y=200)

        registro_button = tk.Button(frame2, text="REGISTRAR", bg="#e0592a", width=15, height=1, command=abrir_registro)
        font_size = font.Font(size=15)
        registro_button["font"] = font_size
        registro_button.place(x=50, y=300)
        registro_button.bind('<Enter>', lambda e: e.widget.config(bg='#FC8A4A'))
        registro_button.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a'))

        juego_button = tk.Button(frame2, text="INICIAR JUEGO", bg="#e0592a", width=15, height=1, command=abrir_menu)
        font_size = font.Font(size=15)
        juego_button["font"] = font_size
        juego_button.place(x=280, y=300)
        juego_button.bind('<Enter>', lambda e: e.widget.config(bg='#FC8A4A'))
        juego_button.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a'))

        imagen_delete = Image.open(help.leerConfig("imagenDelete", "Value"))
        imagen_delete = imagen_delete.resize((60, 60), Image.LANCZOS)
        imagen_delete_tk = ImageTk.PhotoImage(imagen_delete)

        boton = tk.Button(frame2, image=imagen_delete_tk, bg="#e0592a", command=borrar_registro)
        boton.place(x=430, y=480)
        boton.bind('<Enter>', lambda e: e.widget.config(bg='#FC8A4A'))
        boton.bind('<Leave>', lambda e: e.widget.config(bg='#e0592a'))
        #endregion Frame 2
        
        ventana.mainloop()

if __name__ == "__main__":
    VentanaPrincipal()
