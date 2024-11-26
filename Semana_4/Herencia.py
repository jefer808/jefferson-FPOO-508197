from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad, dueno):
        self.nombre = nombre
        self.edad = edad
        self.dueno = dueno

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return 'Guau'

# Instancia de la clase derivada Perro
perro = Perro('Copito', 2, 'Luis')

# Imprimir los detalles del perro
print(perro.nombre, perro.edad, perro.dueno)
print(perro.hacer_sonido())
