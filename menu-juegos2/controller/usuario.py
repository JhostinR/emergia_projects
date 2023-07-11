#Importando librerias necesarias
import os

#Creando una clase
class Usuario:
    def __init__(self):
        self.__nombreUsuario = ""
        self.__direccion = ""
        self.__telefono = ""
        self.__descripcion = ""

    def getNombreUsuario(self):
        return self.__nombreUsuario
    
    def setNombreUsuario(self,nombreUsuario):
        self.__nombreUsuario = nombreUsuario
    
    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self,direccion):
        self.__direccion = direccion
        
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self,telefono):
        self.__telefono = telefono
        
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion

    def imprimirUsuario(self):

        mensaje = (f"El usuario es: {self.getNombreUsuario()}\n")
        mensaje += (f"La direccion es: {self.getDireccion()}\n")
        mensaje += (f"El telefono es: {self.getTelefono()}\n")
        mensaje += (f"La descripcion es: {self.getDescripcion()}")
        print(mensaje) 

    def borrarDatos(self):
        self.nombreUsuario = ""
        self.direccion = ""
        self.telefono = ""
        self.descripcion = ""