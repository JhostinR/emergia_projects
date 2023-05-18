
import os, re

class Correo:
    
    def extraer(self):
        print("----------juego de Extractor de correos----------\n")
        self.text = input("Escribe un texto que contenga correo electronico: ")
    
    def extraido(self):
        self.emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
        print (self.emails)
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()