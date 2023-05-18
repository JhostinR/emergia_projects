import os

class Usuario:
    def __init__(self):
        self.__nombreUsuario = ""
        self.__direccion = ""
        self.__telefono = ""
        self.__descripcion = ""
        self.__numerosJuegos = 0
        
    def getnombreUsuario(self):
        return self.__nombreUsuario
    
    def setnombreUsuario(self,nombreUsuario):
        self.__nombreUsuario = nombreUsuario
    
    def getdireccion(self):
        return self.__direccion
    
    def setdireccion(self,direccion):
        self.__direccion = direccion
        
    def gettelefono(self):
        return self.__telefono
    
    def settelefono(self,telefono):
        self.__telefono = telefono
        
    def getdescripcion(self):
        return self.__descripcion
    
    def setdescripcion(self,descripcion):
        self.__descripcion = descripcion
        
    def getnumerosJuegos(self):
        return self.__numerosJuegos
    
    def setnumerosJuegos(self,numjuegos):
        self.__numerosJuegos = numjuegos

    def pedirDatos(self):
        print("\n")
        self.mensaje =  ("=========================\n")
        self.mensaje += ("|   ESCRIBE TUS DATOS    |\n")
        self.mensaje += ("=========================")
        print(self.mensaje)
        self.setnombreUsuario(input("ingrese su nombre: "))
        self.setdireccion(input("ingrese su direccion: "))
        
        while True:
            try: 
                self.settelefono(int(input("ingrese su telefono: ")))
                break
            except ValueError:
                print("el valor ingresado es incorrecto, intenta ingresar un numero")
        
        self.setdescripcion(input("ingrese su descripcion: "))
        clear = lambda: os.system('cls')
        clear()
    
    def imprimirUsuario(self):
        clear = lambda: os.system('cls')
        clear()
        print("\n")
        self.mensaje =  ("=====================================\n")
        self.mensaje += ("|          DATOS DEL JUGADOR        |\n")
        self.mensaje += ("=====================================")
        print(self.mensaje)
        print(f"El usuario es: {self.getnombreUsuario()}")
        print(f"La direccion del usuario es: {self.getdireccion()}")
        print(f"El telefono de contacto es: {self.gettelefono()}")
        print(f"La descripcion del usuario es: {self.getdescripcion()}")
        print("=====================================")
        return(f"numero de veces que jugo son: {str(self.getnumerosJuegos())}\n=====================================")
