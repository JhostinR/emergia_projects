import json
from PIL import Image, ImageTk
import os 

relative_path = os.getcwd()

class Helpers:

    def __init__(self):
        self.__rutaConfig = relative_path + "/config.json"

    def leerConfig(self, clave, value):
        with open(self.__rutaConfig, 'r') as file: 
            config = json.load(file)
            if config[clave][value] == "":
                print("No esta")
                file.close()
            else:
                dato = str(config[clave][value])
                file.close()
        
        rutaTotal = relative_path + dato
        return rutaTotal

    def getImage(self, relative_path, size):
        image = Image.open(self.leerConfig(relative_path,"Value")).resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    
    def centerWindows(self,windows,height,withs):    
        pantall_ancho = windows.winfo_screenwidth()
        pantall_largo = windows.winfo_screenheight()
        x = int((pantall_ancho/2) - (withs/2))
        y = int((pantall_largo/2) - (height/2))
        return windows.geometry(f"{withs}x{height}+{x}+{y}")
