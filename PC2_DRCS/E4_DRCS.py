# DRCS
# Importamos librerías
import pyfiglet
from colorama import Fore, Back, Style, init

# Creamos título
titulo = pyfiglet.figlet_format("Denilsson")
print(titulo)

class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1 # Almacena el primer numero
        self._num2 = num2 # Almacena el segundo numero

    def suma(self):
        resultado = self._num1 + self._num2 # Suma los dos números
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2  # Suma los dos números
        print(f"El resultado de la suma es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        resultado = self._num1 // self._num2 # Suma los dos números
        print(f"El resultado de la suma es: {self._num1} // {self._num2} = {resultado}")

    def multiplicacion(self):
        resultado = self._num1 * self._num2  # Suma los dos números
        print(f"El resultado de la suma es: {self._num1} * {self._num2} = {resultado}")
# Crear objetos y realizar operaciones
operacion = Calculadora(2 , 2)
operacion.suma()

operacion = Calculadora(4,2)
operacion.resta()

operacion = Calculadora(9,3)
operacion.division()

operacion = Calculadora(8,7)
operacion.multiplicacion()