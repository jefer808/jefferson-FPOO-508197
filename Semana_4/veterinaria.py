class Mascota:
    def __init__(self, nombre, tipo, edad):
        self._nombre = nombre
        self._tipo = tipo
        self.edad = edad

    def __str__(self):
        return f'Mascota: {self._nombre}, Tipo: {self._tipo}, Edad: {self.edad} años'


class Dueño:
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, *mascotas):
        for mascota in mascotas:
            self.mascotas.append(mascota)

    def __str__(self):
        mascotas_info = ""
        for mascota in self.mascotas:
            mascotas_info += str(mascota) + "\n"
        return f"Dueño: {self._nombre}, Teléfono: {self._telefono}\nMascotas:\n{mascotas_info.strip()}"
   

class Consulta:
    def __init__(self, fecha, motivo, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.mascota = mascota

    def __str__(self):
        return f'Consulta: {self.fecha}, Motivo: {self.motivo}, Mascota: {self.mascota._nombre}'



mascota1 = Mascota("Toby", "Perro", 5)
mascota2 = Mascota("Tom", "Gato", 3)


dueno1 = Dueño("Carlos Castillo", 1130645323)
dueno1.agregar_mascota(mascota1, mascota2)


consulta1 = Consulta("2024-10-30", "vacunación", mascota1)
consulta2 = Consulta("2024-10-30", "revisión", mascota2)


print(mascota1)
print(mascota2)
print(dueno1)
print(consulta1)
print(consulta2)
