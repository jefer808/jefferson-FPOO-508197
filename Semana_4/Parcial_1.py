class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}"


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor.nombre}"


class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def obtener_libros_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor == autor]

    def __str__(self):
        return f"Sección: {self.nombre}, Libros: {[libro.titulo for libro in self.libros]}"


# Ejemplo de uso
if __name__ == "__main__":
    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    autor2 = Autor("J.K. Rowling", "Británica")

    libro1 = Libro("Cien años de soledad", autor1)
    libro2 = Libro("El amor en los tiempos del cólera", autor1)
    libro3 = Libro("Harry Potter y la piedra filosofal", autor2)

    seccion_ficcion = Seccion("Ficción")
    seccion_ficcion.agregar_libro(libro1)
    seccion_ficcion.agregar_libro(libro2)
    seccion_ficcion.agregar_libro(libro3)

    print(seccion_ficcion)

    libros_gabo = seccion_ficcion.obtener_libros_por_autor(autor1)
    print("Libros de Gabriel García Márquez en la sección de ficción:")
    for libro in libros_gabo:
        print(libro)
