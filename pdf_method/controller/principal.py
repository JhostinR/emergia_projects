import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

class Visualizador:
    def __init__(self):
        # Crear una ventana de Tkinter
        ventana = tk.Tk()
        ventana.title('Dividir PDF')
        ventana.config(bg='#ffd6dc')
        ventana.configure(width=500, height=300)  # configura tamaño y altura de la ventana
        ventana.geometry("500x300")  # Especificar el tamaño de la ventana

        # Crea un cuadro de entrada para el nombre del archivo PDF
        self.entry_filename = tk.Entry(ventana, width=24)
        self.entry_filename.place(x=175, y=60)

        # Crea un botón para seleccionar el archivo PDF
        button_select_file = tk.Button(ventana, text="𝙎𝙚𝙡𝙚𝙘𝙘𝙞𝙤𝙣𝙖𝙧 𝙖𝙧𝙘𝙝𝙞𝙫𝙤", command=self.select_file, width=18, bg='#ff8a9a')
        button_select_file.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_select_file.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_select_file.place(x=180, y=120)

        # Crea un cuadro de entrada para el número de páginas por PDF
        self.entry_pages_per_pdf = tk.Entry(ventana, width=24)
        self.entry_pages_per_pdf.place(x=175, y=180)

        # Dando una instrucción
        mensaje = tk.Label(ventana, text="Cuantas paginas quieres dividir", font=("Arial", 12, "bold"), foreground="#f7072b", bg="#ffd6dc")
        mensaje.place(x=130, y=205)

        # Crea un botón para dividir el archivo PDF
        button_split_pdf = tk.Button(ventana, text="𝘿𝙞𝙫𝙞𝙙𝙞𝙧", command=self.split_pdf, width=18, height=1, bg='#ff8a9a')
        button_split_pdf.bind('<Enter>', lambda e: e.widget.config(bg='#f7072b'))
        button_split_pdf.bind('<Leave>', lambda e: e.widget.config(bg='#ff8a9a'))
        button_split_pdf.place(x=180, y=260)

        ventana.mainloop()

    # Función para seleccionar el archivo PDF
    def select_file(self):
        # Abre un cuadro de diálogo para seleccionar el archivo PDF
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        # Asigna el nombre del archivo PDF al cuadro de entrada
        self.entry_filename.delete(0, tk.END)
        self.entry_filename.insert(0, filename)

    # Función para dividir el archivo PDF
    def split_pdf(self):
        filename = self.entry_filename.get()
        pages_per_pdf = self.entry_pages_per_pdf.get()

        try:
            # Abrir el archivo PDF
            pdf = PdfReader(open(filename, "rb"))

            # Obtener el número total de páginas del archivo PDF
            total_pages = len(pdf.pages)

            # Validar que el número de páginas por PDF sea un número entero positivo
            if not pages_per_pdf.isdigit() or int(pages_per_pdf) <= 0:
                messagebox.showerror("Error", "Por favor, ingresa un número válido de páginas por PDF.")
                return

            pages_per_pdf = int(pages_per_pdf)

            # Dividir el archivo PDF en partes iguales
            for i in range(0, total_pages, pages_per_pdf):
                # Crear un objeto PDFWriter para el archivo PDF de salida
                writer = PdfWriter()

                # Agregar las páginas al archivo PDF de salida
                for j in range(i, min(i + pages_per_pdf, total_pages)):
                    writer.add_page(pdf.pages[j])

                # Guardar el archivo PDF de salida con un nombre diferente
                output_filename = f"{filename}_({i // pages_per_pdf + 1}).pdf"
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)

            messagebox.showinfo("PDF dividido", "El proceso de división de PDF se ha completado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al dividir el PDF: {str(e)}")

if __name__ == "__main__":
    Visualizador()
