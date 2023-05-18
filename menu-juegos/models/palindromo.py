import os 

class Palindromo:
    
    def inicio(self):
        print("----------juego de los palindromos----------")
        self.texto = input("Ingresa una palabra para verificar si es palindromo: ")
            
    def verificacion(self):
        self.igual, self.aux = 0, 0
        for ind in reversed (range(0,len(self.texto))):
            if self.texto [ind].lower().replace(' ', '') == self.texto[self.aux].lower().replace(' ', ''):
                self.igual += 1
            self.aux += 1
        if len (self.texto) == self.igual:
            print("La palabra es palindromo")
        else:
            print("La palabra no es palindromo") 
    
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()