class Menu:
    def __init__(self):
        self.__titulo = ""
        self.__mensaje = ""
        
    def mostrarTitulo(self):
        self.__titulo =  "=======================================\n"
        self.__titulo += "|         BIENVENIDO AL MENU           |\n"
        self.__titulo += "======================================="
        print(self.__titulo)
        
    def mostrarMenu(self):
        self.__mensaje = "| 0. Salir \n"
        self.__mensaje += "| 1. Par o impar \n"
        self.__mensaje += "| 2. Juego Mad Libs\n"
        self.__mensaje += "| 3. Contador de palabras \n"
        self.__mensaje += "| 4. Información de la biografía \n"
        self.__mensaje += "| 5. ¿Cuál es el acrónimo? \n"
        self.__mensaje += "| 6. Piedra, Papel y tijera \n"
        self.__mensaje += "| 7. Adivina el número \n"
        self.__mensaje += "| 8. ¿Es palíndromo? \n"
        self.__mensaje += "| 9. Calculador de propinas  \n"
        self.__mensaje += "| 10. Extractor de correos electrónicos \n"
        self.__mensaje += "| 11. Generador de letras \n"
        self.__mensaje += "=======================================\n"
        self.__mensaje += "|          ELIGE UNA OPCION           |\n"
        self.__mensaje += "=======================================\n"
        print(self.__mensaje)