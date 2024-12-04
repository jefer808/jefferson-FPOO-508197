class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones_iniciales, energia_generada, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones_iniciales = emisiones_iniciales
        self.emisiones_finales = None  # Inicialmente sin emisiones finales
        self.energia_generada = energia_generada
        self.estado = estado

    def actualizar_emisiones(self, emisiones_finales):
        self.emisiones_finales = emisiones_finales

    def calcular_diferencia_emisiones(self):
        if self.emisiones_finales is not None:
            return self.emisiones_iniciales - self.emisiones_finales
        return None

    def mostrar_informacion(self):
        diferencia_emisiones = self.calcular_diferencia_emisiones()
        impacto_info = (
            f"Diferencia de impacto: {diferencia_emisiones} toneladas reducidas"
            if diferencia_emisiones is not None
            else "Sin emisiones finales registradas"
        )
        return (f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Ubicación: {self.ubicacion}, "
                f"Responsable: {self.responsable.mostrar_informacion()}, Emisiones Iniciales: {self.emisiones_iniciales} toneladas, "
                f"Energía Generada: {self.energia_generada} MWh, Estado: {self.estado}, {impacto_info}")