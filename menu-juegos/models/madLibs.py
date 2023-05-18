import os 

class Madlibs:
    
    def pedirDatos(self):
        print("----------juego de Mad Libs----------")
        
        self.nombre = str(input("ingrese su nombre: "))
        
        while True:
            try: 
                self.edad = int(input("ingrese su edad: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        self.marca = str(input("ingrese la marca de su moto: "))
        
        while True:
            try: 
                self.peso = int(input("ingrese el peso de la moto en Kg: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        while True:
            try:  
                self.cilindraje = int(input("ingrese el cilindraje de la moto Cm3: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        self.color = str(input("ingrese el color de la moto: "))
        
        while True:
            try: 
                self.velocidad = int(input("Ingresa la velocidad de la moto km/h: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        print("\n")
    
    
    def frase(self):
            print(f"Un dia, {self.nombre} compro una motocicleta de color {self.color}, a sus {self.edad} años pudo comprar un vehiculo el cual necesitaba. La motocicleta es una {self.marca}, su cilindraje es de {self.cilindraje} centimetros cubicos, pesa solamente {self.peso} kg y su velocidad maxima es {self.velocidad} km/h.")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()