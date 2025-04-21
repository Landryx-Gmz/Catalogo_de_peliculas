from src.peliculas import Pelicula


class ServicioPeliculas:
    pelicula = Pelicula
    NOMBRE_ARCHIVO = 'peliculas.txt'

    def __init__(self):
        self.peliculas = []

    def guardar_peli_archivo(self, peliculas):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for pelicula in peliculas:
                    archivo.write(f'{pelicula.escribir_pelicula}\n')
        except Exception as e:
            print(f'Error al guardar pelicula en archivo: {e}')

    def agregar_peliculas(self, pelicula):
        self.peliculas.append(pelicula)
