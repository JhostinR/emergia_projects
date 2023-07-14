# --------------------------------------------------
#importacion de clases y librerias necesarias
# --------------------------------------------------
# region
from models.parImpar import ParesImpares
from models.madLibs import Madlibs
from models.contadorPalabras import Palabras
from models.informacionBiografia import Biografia
from models.acronimo import Acronimo
from models.piedraPapelTijera import Piedrapapeltijera
from models.adivinaNumero import adivinarNumero
from models.palindromo import Palindromo
from models.calculadoraPropinas import calcularPropina
from models.extractorCorreos import Correo
from models.generadorLetras import Generador
#endregion

# # --------------------------------------------------
# #clases globales para usar el resistro logs y la impresion de actividades e instancia de metodos
# # --------------------------------------------------
# #region
par = ParesImpares()
madLibs = Madlibs()
contadoraPalabras = Palabras()
informacionBiografia = Biografia()
acronimo = Acronimo()
piedraPapelTijera = Piedrapapeltijera()
adivinaNumero = adivinarNumero()  
palindromo = Palindromo()
calculadoraPropinas = calcularPropina()
extractorCorreos = Correo
generadorLetras = Generador()
# #endregion

class Principal:
    def enviarController(self, opcion):
            
            if opcion == 1:
                par.pedirNumero()
                par.esPar()
                par.continuar()
                
            if opcion == 2:
                madLibs.pedirDatos()
                madLibs.frase()
                madLibs.continuar()
            
            if opcion == 3:
                contadoraPalabras.pedirTexto()
                contadoraPalabras.frase()
                contadoraPalabras.continuar()
            
            if opcion == 4:
                informacionBiografia.pedirDatos()
                informacionBiografia.frase()
                informacionBiografia.continuar()
            
            if opcion == 5:
                acronimo.escribirAcronimo()
                acronimo.esAcronimo()
                acronimo.resultado()
                acronimo.continuar()
            
            if opcion == 6:
                piedraPapelTijera.Datos()
                piedraPapelTijera.juego()
                piedraPapelTijera.continuar()
            
            if opcion == 7:
                adivinaNumero.adivinar_numero()
                adivinaNumero.continuar()
            
            if opcion == 8:
                palindromo.inicio()
                palindromo.verificacion()
                palindromo.continuar()
            
            if opcion == 9:
                calculadoraPropinas.escribirTotal()
                calculadoraPropinas.totales()
                calculadoraPropinas.resultados()
                calculadoraPropinas.calculoFinal()
                calculadoraPropinas.continuar()
            
            if opcion == 10:
                extractorCorreos.extraer(self)
                extractorCorreos.extraido(self)
                extractorCorreos.continuar(self)
            
            if opcion == 11:
                generadorLetras.generador_letras()
                generadorLetras.resultado()
                generadorLetras.continuar()