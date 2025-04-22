from src.peliculas import Pelicula
from src.servicio_peliculas import ServicioPeliculas


class CatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def motrar_menu(self):
        print('***Catalogo de Peliculas***\n')
        while True:
            try:
                print(f'''Opciones: 
                1. Agregar Película
                2. Listar Película
                3. Eliminar Pelicula
                4. Salir''')
                opcion = int(input('Porfavor elija una opción: '))
                if opcion == 1:
                    nombre_pelicula = input('Nombre pelicula: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_peliculas(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Gracias por utilizar nuestros servicios')
                    break
                else:
                    print('Opcion invalida introduce un valor entre 1 y 4')

            except ValueError:
                print('Error: Introduce un número válido')
            except Exception as e:
                print(f'Ocurrió un error: {e}')


# Agregamos el bloque main
if __name__ == '__main__':
    app = CatalogoPeliculas()
    app.motrar_menu()
