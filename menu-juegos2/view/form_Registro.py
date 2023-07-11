import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, scrolledtext
from models.util.Helpers import Helpers
from controller.usuario import Usuario

help = Helpers()

class Registro:
    def __init__(self, ventana, datos_label):
        ventana = Toplevel(ventana)
        usuario = Usuario()
        super().__init__()

        # region configuracion de la ventana
        ventana.title("Registro de Jugador")
        ventana.geometry("600x450")
        ventana.configure(bg='#bfabf7')
        ventana.resizable(False, False)
        help.centerWindows(ventana, 450, 600)
        # endregion configuracion de la ventana

        # region registrar datos
        def validarDatos():
            if nombre_entry.get() == "" or None:
                return False
            if direccion_entry.get() == "" or None:
                return False
            if telefono_entry.get() == "" or None:
                return False
            else:
                return True

        def registrar_datos():
            if validarDatos():
                
                nameUsuario = str(nombre_entry.get())
                direccion = str(direccion_entry.get())
                telefono = str(telefono_entry.get())
                descripcion = str(descripcion_text.get("1.0", tk.END))

                usuario.setNombreUsuario(nameUsuario)
                usuario.setDireccion(direccion)
                usuario.setTelefono(telefono)
                usuario.setDescripcion(descripcion)

                messagebox.showinfo("Registro exitoso", "Los datos del jugador se han registrado correctamente.")
                
                datos_label.config(text=f"Su nombre es: {usuario.getNombreUsuario()}\n"
                                        f"Su dirección es: {usuario.getDireccion()}\n"
                                        f"Su teléfono es: {usuario.getTelefono()}\n"
                                        f"Su descripción es: {usuario.getDescripcion()}")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                ventana.lift()
        # endregion registrar datos

        # region limpiar datos
        def limpiar_datos():
            nombre_entry.delete(0, tk.END)
            direccion_entry.delete(0, tk.END)
            telefono_entry.delete(0, tk.END)
            descripcion_text.delete("1.0", tk.END)
        # endregion limpiar datos

        # region frame superior
        frameHeader = tk.Frame(ventana, bd=0, height=80, relief=tk.SOLID, padx=1, pady=1, bg='#8a36d2')
        frameHeader.pack(side="top", expand=tk.FALSE, fill=tk.BOTH)

        logoemergia = help.getImage("imagenNavBar", (380, 70))
        label = tk.Label(frameHeader, image=logoemergia, bg="#8a36d2")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        # endregion frame superior

        # region Frame 1
        frame1 = tk.Frame(ventana, bg='#ff9e18')
        frame1.place(x=0, y=80, width=300, height=430)

        imgJuegos = Image.open(help.leerConfig("imagenJuegos", "Value"))
        nueva_imagen = imgJuegos.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)

        label = tk.Label(frame1)
        label.place(x=40, y=100)
        label.config(image=imagen_tk, bg="#ff9e18")

        titulo = tk.Label(frame1, text="ミ DATOS DEL JUGADOR 彡", font=("Helvetica", 16, "bold"), bg="#ff9e18",
                          foreground="#773dbd")
        titulo.place(x=0, y=20)
        # endregion Frame1

        # region Frame2

        # Frame para el resto de los elementos
        frame2 = tk.Frame(ventana, bg='#773dbd')
        frame2.place(x=300, y=80, width=300, height=420)

        nombre_label = tk.Label(frame2, text="Nombre:", bg="#773dbd", foreground="#ff9e18",
                                font=("Helvetica", 11, "bold"))
        nombre_label.place(x=115, y=5)
        nombre_entry = tk.Entry(frame2, bg="#773dbd", foreground="#fff", font=("Helvetica", 11, "bold"))
        nombre_entry.place(x=65, y=35)

        # Dirección y etiqueta de la dirección
        direccion_label = tk.Label(frame2, text="Dirección:", bg="#773dbd", foreground="#ff9e18",
                                   font=("Helvetica", 11, "bold"))
        direccion_label.place(x=110, y=65)
        direccion_entry = tk.Entry(frame2, bg="#773dbd", foreground="#fff", font=("Helvetica", 11, "bold"))
        direccion_entry.place(x=65, y=95)

        # Teléfono y etiqueta del teléfono
        telefono_label = tk.Label(frame2, text="Teléfono:", bg="#773dbd", foreground="#ff9e18",
                                  font=("Helvetica", 11, "bold"))
        telefono_label.place(x=110, y=130)
        telefono_entry = tk.Entry(frame2, bg="#773dbd", foreground="#fff", font=("Helvetica", 11, "bold"))
        telefono_entry.place(x=65, y=155)

        # Descripción y etiqueta de la descripción
        descripcion_label = tk.Label(frame2, text="Descripción (opcional):", bg="#773dbd", foreground="#ff9e18",
                                     font=("Helvetica", 11, "bold"))
        descripcion_label.place(x=65, y=190)
        descripcion_text = scrolledtext.ScrolledText(frame2, width=20, height=4, bg="#773dbd", foreground="#fff",
                                                     font=("Helvetica", 11, "bold"))
        descripcion_text.place(x=60, y=220)

        # Botón para registrar los datos
        registrar_button = tk.Button(frame2, text="REGISTRAR", font=("Helvetica", 9, "bold"), bg="#773dbd",
                                     foreground="#fff", width=13, height=1, command=registrar_datos)
        registrar_button.place(x=20, y=325)
        registrar_button.bind('<Enter>', lambda e: e.widget.config(bg='#9d79ff', foreground="#000"))
        registrar_button.bind('<Leave>', lambda e: e.widget.config(bg='#7141f5', foreground="#fff"))

        limpiar_button = tk.Button(frame2, text="LIMPIAR", font=("Arial", 9, "bold"), bg="#FC8A4A", width=13, height=1,
                                   command=limpiar_datos)
        limpiar_button.place(x=180, y=325)
        limpiar_button.bind('<Enter>', lambda e: e.widget.config(bg='#e0592a', foreground="#fff"))
        limpiar_button.bind('<Leave>', lambda e: e.widget.config(bg='#FC8A4A', foreground="#000"))
        # endregion Frame2

        ventana.mainloop()