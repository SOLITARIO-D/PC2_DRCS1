# DRCS
# Importamos librerías
import pyfiglet
from colorama import Fore, Back, Style, init

# Creamos título
titulo = pyfiglet.figlet_format("Denilsson")
print(titulo)

# Damos color al texto y estilo
print( Fore.RED + Style.BRIGHT)
# Se define la clase llamada Estuadiante
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultado(self):
        if self.nota >= 60:
            print("¡HAS APROBADO!")
        else:
            print("¡HAS REPROBADO!")

# Crear primer objeto estudiantes
estudiante1 = Estudiante("Pedro", 60)
estudiante1.imprimir()
estudiante1.resultado()