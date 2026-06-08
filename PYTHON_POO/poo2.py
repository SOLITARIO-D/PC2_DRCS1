# Constructores en Python
# Constructor: Metodo especial _init_ que
# se ejecuta al crear un objeto

# def: define un metodo
# init: Constructor
# self: Representa el conector actual
# nombre, salario son datos recibidos

# Creando una clase Empleado
class Empleado:
    def __init__(self,nombre,salario):
        # self permite acceder a los atributos
        # del objeto
        self.nombre = nombre
        self.salario = salario
