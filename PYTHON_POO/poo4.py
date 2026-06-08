# Atributos y Métodos de la Clase en Python
# Atributos de clase: Compartimpos por todos los objetos

# Se crea una clase llamada Empleado
# Servira para crear Objetos
class Empleado:
    # Se crea un atributo de clase
    # Este atributo pertenece a toda la clase
    # y no a un objeto especifico
    # Todos los empleados compartiran este mismo valor
    empresa = "Intelaf"

    # Indica que el metodo es de la clase
    # el metodo trabjara con la clase y no
    # con objetos individuales
    @classmethod

    # Se define un metodo de clase llamado mostrar_empresa
    # cls representa la clase Empleado
    def mostrar_empresa(cls):
        # Devuelve el valor del atributo de clase empresa
        return cls.empresa