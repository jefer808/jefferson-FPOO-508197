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
    def __init__(self, nombre, edad, dueno, raza, color):
        super().__init__(nombre, edad, dueno)
        self.raza = raza
        self.color = color

    def hacer_sonido(self):
        return 'Guau'

# Instancia de la clase derivada Perro con todos los argumentos necesarios
perro = Perro('Copito', 2, 'Luis', 'Golden Retriever', 'Dorado')

# Imprimir los detalles del perro
print(perro.nombre, perro.edad, perro.dueno, perro.raza, perro.color)
print(perro.hacer_sonido())
