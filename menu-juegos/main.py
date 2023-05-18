# ------------------------------------------------------------
#importacion de clases y librerias necesarias Proyectos
# ------------------------------------------------------------
# region
from models.menu import Menu
from controller.principal import Principal
from controller.usuario import Usuario
import os 
#endregion

# ----------------------------------------------------------------------------------------------------
#clases globales para usar el resistro logs y la impresion de actividades e instancia de metodos
# ----------------------------------------------------------------------------------------------------
#region
menu = Menu()
principal = Principal()
opcion = 1
numero = 0
usuario = Usuario()
#endregion

#instancias objeto




# --------------------------------------------------
#Metodo main
# --------------------------------------------------
#region
def main(opcion,numero):
    
    usuario.pedirDatos()
    usuario.imprimirUsuario()

    while opcion !=0:
        menu.mostrarTitulo()
        menu.mostrarMenu()
        try:
            opcion = int(input())
        except ValueError as ex:
            clear = lambda: os.system('cls')
            clear()
            print("el valor es no numerico Error:" + str(ex))
            print("oprime una tecla para continuar")
            input()
    
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7 or opcion == 8 or opcion == 9 or opcion == 10 or opcion == 11:
            
            contador = usuario.getnumerosJuegos()
            contador = contador + 1
            usuario.setnumerosJuegos(contador)
            numero = numero + 1
            
            clear = lambda: os.system('cls')
            clear()
            principal.enviarController(opcion)
        else:
            clear = lambda: os.system('cls')
            clear()
            print ("tu opcion es incorrecta elige otra")
    
    clear = lambda: os.system('cls')
    clear()
    mensaje1 = usuario.imprimirUsuario()
    print(f"{mensaje1}")
    mensaje2 =  "=====================================\n"
    mensaje2 += "|     ADIOS, GRACIAS POR JUGAR      |\n"
    mensaje2 += "=====================================\n"
    print(mensaje2)
#endregion

#metodo para iniciar el metodo main
if __name__ == '__main__':
    main(opcion,numero) 