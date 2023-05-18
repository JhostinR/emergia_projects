import os 
import random

class Piedrapapeltijera:
    def Datos(self):
        print("----------juego de Piedra, papel o tijeras----------")
        self.opciones = ["piedra", "papel", "tijera"]
        self.resultados =  {"piedra": {"piedra": "empate", "papel": "perder", "tijera": "ganaste"},
                            "papel": {"piedra": "ganar", "papel": "empate", "tijera": "perdiste"},
                            "tijera": {"piedra": "perder", "papel": "ganar", "tijera": "ha sido un empate"}}
        
    def juego(self):
        usuario = input("Elige piedra, papel o tijera: ").lower()
        while usuario not in self.opciones:
            usuario = input("Esa no es una opción válida. Elige piedra, papel o tijera: ").lower()
        pc = random.choice(self.opciones)
        resultado = self.resultados[usuario][pc]
        print(f"Tú elegiste {usuario}. La computadora eligió {pc}. Resultado: {resultado}")
        
        if resultado == "ganaste":
            return 1
        elif resultado == "ha sido un empate":
            return 0
        else:
            return -1
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()