import pandas as pd
from os import system

class DatosProcessor:
    def __init__(self, datos):
        self.datos = datos
    
    def formatear_valores(self):
        for monitor in self.datos:
            for key, value in monitor.items():
                if (key == "Cuotas" or key == "Cuotas sin interes") and value == "No disponible":
                    pass
                elif key == "Cuotas":
                    valorLista = value.split("$")
                    value = f"{valorLista[0]}${valorLista[-1]}"
                    monitor[key] = value
                elif key == "Cuotas sin interes":
                    valorLista = value.split("$")
                    value = f"{valorLista[0]}${valorLista[-1]}"
                    monitor[key] = value
    
    def guardar_en_excel(self, filename):
        df = pd.DataFrame(self.datos)
        df.to_excel(filename, sheet_name="Monitores")
    
    def abrir_excel(self, filename):
        system(filename)