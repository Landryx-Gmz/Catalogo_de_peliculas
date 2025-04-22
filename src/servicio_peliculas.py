import os


class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_peliculas(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
            print("Pelicula agregada correctamente")

    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('-----Listado de peliculas-----')
            print(archivo.read())

    def eliminar_archivo_peliculas(self):
        os.remove(self.nombre_archivo)
        print(f'Archivo elimnado: {self.nombre_archivo}')
