# Clase Proyecto
class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones, energia_generada, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones = emisiones
        self.energia_generada = energia_generada
        self.estado = estado

    def actualizar_emisiones(self, nuevas_emisiones):
        self.emisiones = nuevas_emisiones

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_informacion(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, " \
               f"Ubicación: {self.ubicacion}, Responsable: {self.responsable}, " \
               f"Emisiones: {self.emisiones}, Energía Generada: {self.energia_generada}, Estado: {self.estado}"
