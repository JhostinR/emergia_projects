import os 

class Palabras:
    def pedirTexto(self):
        print("----------juego de contar las palabras----------")
        self.texto = input("Introduce un texto: ")
        self.num_palabras = len(self.texto.split())
    
    def frase(self):
        print(f"El texto tiene {self.num_palabras} palabras.")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()