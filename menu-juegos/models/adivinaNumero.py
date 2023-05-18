import random
import os

class adivinarNumero:

    def adivinar_numero(self):
        self.numero_secreto = random.randint(1, 20)  # Generar un número aleatorio entre 1 y 20
        self.intentos = 0

        print("----------juego de Adivinar el numero----------\n")
        print("¡Adivina el número secreto entre 1 y 20!\n")

        while True:
            intento = int(input("Introduce tu intento: "))
            self.intentos += 1

            if intento < self.numero_secreto:
                print("El número secreto es mayor. ¡Sigue intentándolo!")
            elif intento > self.numero_secreto:
                print("El número secreto es menor. ¡Sigue intentándolo!")
            else:
                print(f"¡Felicidades! Adivinaste el número secreto en {self.intentos} intentos.")
                break
            
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()