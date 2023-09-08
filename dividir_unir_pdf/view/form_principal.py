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
        # Crear una ventana de Tkinter
        self.ventana = tk.Tk()
        super().__init__()
        self.ventana.title('Dividir PDF')
        self.ventana.config(bg='#ffd6dc')
        self.ventana.configure(width=500, height=400)  # configura tamaño y altura de la ventana
        self.ventana.geometry("500x400")  # Especificar el tamaño de la ventana
        self.ventana.resizable(False,False)
        help.centerWindows(self.ventana,400,500) # height width
        
        # Llama el icono de la ventana
        logo = help.getImage("imagenPDF", (200, 200))
        self.ventana.iconphoto(True, logo)
        
        imagen = Image.open(help.leerConfig("imagenPrincipal", "Value"))
        nueva_imagen = imagen.resize((270, 270))
        imagen_tk = ImageTk.PhotoImage(nueva_imagen)
        
        label = tk.Label(self.ventana)
        label.place(x=100, y=80)
        label.config(image=imagen_tk, bg="#ffd6dc")
        
        # Titulo principal
        titulo = tk.Label(self.ventana, text="Dιʋιԃιɾ PDF", font=("Arial", 26, "bold"), foreground="#f5425d", bg="#ffd6dc")
        titulo.place(x=150,y=8)

        # Crea un botón para dividir el archivo PDF
        button_dividir_pdf = tk.Button(self.ventana, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", font=("Arial", 14, "bold"), command=self.dividirPDF, width=10, bg='#ff8a9a')
        button_dividir_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_dividir_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_dividir_pdf.place(x=60, y=300)
        
        # Crea un botón para unir el archivo PDF
        button_unir_pdf = tk.Button(self.ventana, text="𝙐𝙣𝙞𝙧 𝙋𝘿𝙁", font=("Arial", 14, "bold"), command=self.unirPDF, width=10, bg='#ff8a9a')
        button_unir_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_unir_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_unir_pdf.place(x=320, y=300)
        
        self.ventana.mainloop()
        
    def dividirPDF(self):
        self.ventana.withdraw()
        dividir_pdf = PDFDividerApp()
        dividir_pdf.mainloop()
    
    def unirPDF(self):
        self.ventana.withdraw()  # Oculta la ventana actual
        pdf_unir_app = PDFUnirApp()
        pdf_unir_app.mainloop()  # Abre la ventana de la clase PDFUnirApp en modo modal

if __name__ == "__main__":
    Visualizador()