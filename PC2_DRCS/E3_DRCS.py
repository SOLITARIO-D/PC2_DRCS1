# DRCS
# Importamos librerías
import pyfiglet
from colorama import Fore, Back, Style, init

# Creamos título
titulo = pyfiglet.figlet_format("Denilsson")
print(titulo)

# Damos color al texto y estilo
print( Fore.WHITE + Style.BRIGHT)

# Se define la clase llamada Persona
class Persona:
    def __init__(self, n, e):
        self.nombre = n # Asigna el nombre recibido
        self.edad = e   # Asigna la edad recibida

    def cumpleaños(self):
        self.edad += 1 # Incrementa la edad en 1

p = Persona(input("Ingrese el nombre: "), int(input("Ingrese edad: ")))

# Llama dos veces al metodo cumpleaños para sumar 2 años
p.cumpleaños()
p.cumpleaños()

# Muestra el resultado con un mensaje bien formado
print(f"{p.nombre} cumple {p.edad} años")
