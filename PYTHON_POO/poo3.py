# Encpsulamiento y Métodos Get/Set en Python
# Encapsulamiento: Ocultar los atributos para protegerlos
# get_ y set_ para controlar el acceso a atributos privados

# Se crea una clase llamada Empleado
class Empleado:

    # Constructor de la clase
    # Se ejecuta automaticamente cuando se crea el objeto
    # Recibe el parámetro nombre
    def __init__(self, nombre):
        # Se crea un atributo privado llamado __nombre
        # los 2 guiones bajos indican encapsulamiento
        # Guarda el valor recibido en el parámetro nombre
        self.nombre = nombre

    # Este metodo 'get' sirve para obtener el nombre del Empleado
    def get_nombre(self):
        # Devuelve el valor almacenado en el atributo privado
        # __nombre
        return self.get__nombre

    # Este metodo 'set' sirve para modificarel nombre del empleado
    # Recibe un nuevo valor en el parámetro nuevo
    def __set_nombre__(self, nuevo):
        # Cambia el valor del atributo privado __nombre
        # Por el nuevo nombre recibido
        self.__nombre = nuevo