class Calculadora:
    def __init__(self):
        self.peso=int(input("dame tu peso en kilos:"))
        self.altura=int(input("dame altura en cm:"))

        self.num1=int(input("numero 1:"))
        self.num2=int(input("numero 2:"))
    def calcularIMC(self):
        self.imc=self.peso/(self.altura*self.altura)
        print("tu IMC es:",self.imc)
        if self.imc < 18.5:
            print("Bajo peso")
        elif self.imc < 25:
            print("Peso normal")
        elif self.imc < 30:
            print("Sobrepeso")
        else:
            print("Obesidad")
    def sumar(self):
        self.suma=self.num1+self.num2
        print("La suma es:", self.suma)
    def restar(self):
        self.resta=self.num1-self.num2
        print("La resta es:", self.resta)
        print("Prueba de cambios para ver si se sube")
