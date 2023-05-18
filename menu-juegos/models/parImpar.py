import os 

class ParesImpares:
    
    def pedirNumero(self):
        print("----------juego de par e impar----------")
        self.num = int(input("escribe un numero: "))
    
    def esPar(self):
        if self.num % 2 == 0:
            print(f"el numero es par")
        else:
            print(f"el numero es impar")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()