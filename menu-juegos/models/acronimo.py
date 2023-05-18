import os
class Acronimo:
    def escribirAcronimo(self):
        print("----------juego de acronimos----------")
        self.frase = input("Escribe la frase que quieres convertir en acronimo: ")
        
    def esAcronimo(self):
        self.palabras = self.frase.split()
        self.acr = ""
        
    def resultado(self):
        for self.palabra in self.palabras:
            self.acr += self.palabra[0].upper()
        print(self.acr)
        
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()