import os 

class Biografia:
    
    def pedirDatos(self):
        print("----------juego de biografia----------")
        
        self.nombre = input("ingrese su nombre: ")
        
        while True:
            try: 
                self.dia = int(input("ingrese su dia de nacimiento: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        self.mes = input("ingrese su mes de nacimiento: ")
        
        while True:
            try: 
                self.año = int(input("ingrese su año de nacimiento: "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        self.profesion = input("cual es su profesion? ")
        
        self.lugarNacimiento = input("ingrese su lugar de nacimiento: ")
        
        self.lugarEstudio = input("ingrese el lugar donde se graduo (universidad, institucion, etc): ")
        
        self.nombreMadre = input("ingrese el nombre de su madre: ")
        
        self.nombrePadre = input("ingrese el nombre de su padre: ")
        
        while True:
            try: 
                self.numHermanos = int(input("cuantos hermanos tiene? "))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        print("\n")
        
    def frase(self):
            print(f"{self.nombre} nacio el {self.dia} de {self.mes} del año {self.año}, en {self.lugarNacimiento}. Es un/una {self.profesion} el cual se graduo en {self.lugarEstudio}. su madre se llama {self.nombreMadre} y su padre {self.nombrePadre} y tiene en total {self.numHermanos} hermano/s")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()