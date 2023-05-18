import random, string, os

class Generador:
    def generador_letras(self):
        self.rstr = random.choice(string.ascii_letters)
    
    def resultado(self):
        print("----------juego de generar letras----------")
        print(f"la letra que ha sido generada es: '{self.rstr}'")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()