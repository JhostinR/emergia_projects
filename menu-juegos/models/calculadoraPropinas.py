import os

class calcularPropina:
    def escribirTotal(self):
        print("----------juego de calcular propinas----------")
        
    def totales(self):
        self.valor_a_pagar = int(input("Ingresa el valor total de la factura o monto: $"))
        self.porcentaje_propina = int(input("Ingrese el porcentaje de propina que quieres dar:%"))
        # self.compartir_factura = int(input("Ingrese entre cuantas personas quieres dividir el pago?: "))
        
    def resultados(self):
        # self.resultado1 = (self.valor_a_pagar / self.compartir_factura)
        # self.resultado2 = (self.resultado1 * self.porcentaje_propina / 100)
        self.totalPropina = (self.valor_a_pagar * (self.porcentaje_propina / 100))
    
    def calculoFinal(self):
        # self.calculoFinal = round(self.resultado2 + self.resultado1)
        print(f"El valor total es {self.valor_a_pagar} y se le sumara {self.totalPropina}")
    
    def continuar(self):
        print("------------------------------")
        print("oprime enter para continuar")
        print("------------------------------")
        input()
        clear = lambda: os.system('cls')
        clear()