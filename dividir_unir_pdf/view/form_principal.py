import tkinter as tk
from util.helpers import Helpers
from PIL import Image, ImageTk
from view.form_unir import PDFUnirApp
from view.form_dividir import PDFDividerApp

unir = PDFUnirApp
dividir = PDFDividerApp
help = Helpers()

class Visualizador:
    def __init__(self):
        # Crear una ventana_principal de Tkinter
        self.ventana_principal = tk.Tk()
        super().__init__()
        self.ventana_principal.title('Dividir PDF')
        self.ventana_principal.config(bg='#ffd6dc')
        self.ventana_principal.configure(width=500, height=400)  # configura tamaño y altura de la ventana_principal
        self.ventana_principal.geometry("500x400")  # Especificar el tamaño de la ventana_principal
        self.ventana_principal.resizable(False,False)
        help.centerWindows(self.ventana_principal,400,500) # height width
        
        # Llama el icono de la ventana_principal
        logo = help.getImage("imagenPDF", (200, 200))
        self.ventana_principal.iconphoto(True, logo)
        
        imagen = Image.open(help.leerConfig("imagenPrincipal", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)
        
        label = tk.Label(self.ventana_principal)
        label.place(x=100, y=80)
        label.config(image=imagen_tk, bg="#ffd6dc")
        
        # Titulo principal
        titulo = tk.Label(self.ventana_principal, text="Dιʋιԃιɾ PDF", font=("Arial", 26, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=150,y=8)

        # Crea un botón para dividir el archivo PDF
        button_dividir_pdf = tk.Button(self.ventana_principal, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", font=("Arial", 14, "bold"), command=self.dividirPDF, width=10, bg='#ff8a9a')
        button_dividir_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_dividir_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_dividir_pdf.place(x=60, y=300)
        
        # Crea un botón para unir el archivo PDF
        button_unir_pdf = tk.Button(self.ventana_principal, text="𝙐𝙣𝙞𝙧 𝙋𝘿𝙁", font=("Arial", 14, "bold"), command=self.unirPDF, width=10, bg='#ff8a9a')
        button_unir_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_unir_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_unir_pdf.place(x=320, y=300)
        
        self.ventana_principal.mainloop()
        
    def dividirPDF(self):
        self.ventana_principal.withdraw()  # Oculta la ventana_principal principal
        dividir_pdf = PDFDividerApp(self.ventana_principal)  # Pasa la ventana_principal principal como argumento
    
    def unirPDF(self):
        self.ventana_principal.withdraw()  # Oculta la ventana_principal actual
        pdf_unir_app = PDFUnirApp(self.ventana_principal)

if __name__ == "__main__":
    Visualizador()
