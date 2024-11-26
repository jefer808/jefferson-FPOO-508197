from Models.Responsable import Responsable  # Importa la clase del responsable módulo Models.Responsable
from Models.Proyecto import Proyecto  # Importa la clase Proyecto desde el módulo Models.Proyecto


# Clase Organización
# Clase Organización
class Organizacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def eliminar_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                self.proyectos.remove(proyecto)
                print(f"Proyecto con ID {id_proyecto} eliminado exitosamente.")
                return
        print(f"No se encontró un proyecto con el ID {id_proyecto}.")

    def calcular_total_emisiones(self):
        return sum(p.emisiones for p in self.proyectos)

    def ordenar_proyectos_por_impacto(self):
        self.proyectos.sort(key=lambda p: p.emisiones, reverse=True)

    def mostrar_proyectos_completados(self):
        return [p for p in self.proyectos if p.estado == "Completado"]

    def mostrar_todos_los_proyectos(self):
        return [p.mostrar_informacion() for p in self.proyectos]

    def comparar_impacto(self, id_proyecto1, id_proyecto2):
        proyecto1 = next((p for p in self.proyectos if p.id == id_proyecto1), None)
        proyecto2 = next((p for p in self.proyectos if p.id == id_proyecto2), None)

        if proyecto1 and proyecto2:
            if proyecto1.emisiones > proyecto2.emisiones:
                return f"El proyecto '{proyecto1.nombre}' tiene mayor impacto con {proyecto1.emisiones} toneladas reducidas."
            elif proyecto1.emisiones < proyecto2.emisiones:
                return f"El proyecto '{proyecto2.nombre}' tiene mayor impacto con {proyecto2.emisiones} toneladas reducidas."
            else:
                return f"Ambos proyectos tienen el mismo impacto con {proyecto1.emisiones} toneladas reducidas."
        else:
            return "Uno o ambos proyectos no se encontraron."


# Menú Interactivo
def menu():
    organizacion = Organizacion("GreenTech Global")
    
    while True:
        print("\n--- Sistema de Gestión de Proyectos de Energías Renovables ---")
        print("1. Agregar Proyecto")
        print("2. Mostrar Información de Proyectos")
        print("3. Actualizar Estado de un Proyecto")
        print("4. Calcular Total de Emisiones Reducidas")
        print("5. Ordenar Proyectos por Impacto")
        print("6. Mostrar Proyectos Completados")
        print("7. Eliminar Proyecto")
        print("8. Comparar Impacto entre Proyectos")
        print("9. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            id = input("ID del proyecto: ")
            nombre = input("Nombre del proyecto: ")
            tipo = input("Tipo de energía (solar, eólica, etc.): ")
            ubicacion = input("Ubicación: ")
            
            # Datos del responsable
            print("\n--- Datos del Responsable ---")
            dni = input("DNI: ")
            nombre_responsable = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            responsable = Responsable(dni, nombre_responsable, apellido, email, telefono)
            
            emisiones = float(input("Emisiones reducidas (toneladas): "))
            energia_generada = float(input("Energía generada (MWh): "))
            estado = input("Estado (Activo/Completado): ")
            
            proyecto = Proyecto(id, nombre, tipo, ubicacion, responsable, emisiones, energia_generada, estado)
            organizacion.agregar_proyecto(proyecto)
            print("Proyecto agregado exitosamente.")
        
        elif opcion == "2":
            proyectos = organizacion.mostrar_todos_los_proyectos()
            if proyectos:
                print("\n--- Lista de Proyectos ---")
                for proyecto in proyectos:
                    print(proyecto)
            else:
                print("\nNo hay proyectos registrados.")
        
        elif opcion == "3":
            id = input("ID del proyecto a actualizar: ")
            nuevo_estado = input("Nuevo estado (Activo/Completado): ")
            for proyecto in organizacion.proyectos:
                if proyecto.id == id:
                    proyecto.cambiar_estado(nuevo_estado)
                    print("Estado actualizado exitosamente.")
                    break
            else:
                print("Proyecto no encontrado.")
        
        elif opcion == "4":
            total_emisiones = organizacion.calcular_total_emisiones()
            print(f"Total de emisiones reducidas: {total_emisiones} toneladas.")
        
        elif opcion == "5":
            organizacion.ordenar_proyectos_por_impacto()
            print("\n--- Proyectos Ordenados por Impacto (Emisiones Reducidas) ---")
            for proyecto in organizacion.proyectos:
                print(proyecto.mostrar_informacion())
        
        elif opcion == "6":
            completados = organizacion.mostrar_proyectos_completados()
            if completados:
                print("\n--- Proyectos Completados ---")
                for proyecto in completados:
                    print(proyecto.mostrar_informacion())
            else:
                print("No hay proyectos completados.")
        
        elif opcion == "7":
            id_proyecto = input("ID del proyecto a eliminar: ")
            organizacion.eliminar_proyecto(id_proyecto)
        
        elif opcion == "8":
            id_proyecto1 = input("ID del primer proyecto: ")
            id_proyecto2 = input("ID del segundo proyecto: ")
            resultado = organizacion.comparar_impacto(id_proyecto1, id_proyecto2)
            print(resultado)
        
        elif opcion == "9":
            print("Saliendo del sistema")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
