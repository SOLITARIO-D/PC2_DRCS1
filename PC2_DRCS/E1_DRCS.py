# DRCS
# Importamos librerías
import pyfiglet
from colorama import Fore, Back, Style, init

# Creamos título
titulo = pyfiglet.figlet_format("Denilsson")
print(titulo)

# Damos color al texto y estilo
print( Fore.LIGHTGREEN_EX + Style.DIM)
# Crear una clase Alumno con nombre y promedio en Python
# Se define la clase llamada Alumno
class Alumno:
    # Metodo constructor que se ejecutara automaticamente al crear un nuevo objeto
    def __init__(self, nombre, promedio):
        # Se crea un atributo llamado 'nombre' y se le asigna el valor recibido por parámetro
        self.nombre = nombre

        # Se crea un atributo llamado 'promedio' y se le asigna el valor recibido por parámetro
        self.promedio = promedio

    # Metodo para obtener el promedio del alumno
    def obtener_promedio(self):
        return self.promedio
    # Metodo para obtener el nombre del alumno (getter)
    def obtener_nombre(self):
        return self.nombre # Devuelve el nombre almacenado en el atributo

    # Metodo para obtener el promedio del alumno (setter)
    def cambiar_promedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio # Se actualiza el valor del atributo 'promedio'

# Se solicita al usuario que ingrese el npmbre del alumno
nombre_ingresado = input(" > Ingrese el nombre del alumno: ")

# Se solicita al usuario que ingrese el promedio del alumno, convirtiendolo a float
promedio_ingresado = float(input(" > Ingrese el promedio del alumno: "))

# Se crea un objeto de la clase Alumno con los datos ingresados por el usuario
alumno1 = Alumno(nombre_ingresado, promedio_ingresado)

# Se muestra el nombre del alumno usando el metodo obtener_nombre()
print("Nombre del Alumno: ", alumno1.obtener_nombre())

# Se muestra el promedio del alumno usando el metodo obtener_promedio()
print("Nombre del Alumno: ", alumno1.obtener_promedio())

# Se solicita un nuevo promedio al usuario para modificar el dato existente
nuevo_promedio = float(input(" > Ingrese un nuevo promedio para el alumno: "))

# Se llama al metodo cambiar_promedio para actualizar el promedio del alumno
alumno1.cambiar_promedio(nuevo_promedio)

# Se muestra el nuevo promedio actualizado
print(" Nuevo promedio actualizado: ", alumno1.obtener_promedio())