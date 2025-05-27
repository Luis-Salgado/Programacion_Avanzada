#Práctica 4, métodos mágicos

#1. Implemente una clase Rectangulo que represente un rectángulo y que tenga dos
#atributos base y altura. Use __eq__ para comparar si dos rectángulos son iguales
#(misma base y altura) y __ne__ para verificar si son diferentes. Utilice los métodos
#__gt__ y __lt__ para comparar el área de dos rectángulos, devuelva True o False
#según sea el caso.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __eq__(self, other):
        return self.base == other.base and self.altura == other.altura

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()
    def area(self):
        return self.base * self.altura
 
import os
os.system('clear')
print ("")
print ("")
print ("Bienvenido a la comparación de Rectángulos")
print ("-------------------")
print("A continuación se compararán dos rectángulos")
# Solicitar las dimensiones de los rectángulos
print("Ingrese las dimensiones del primer rectángulo:")
base1 = float(input("Base: "))
altura1 = float(input("Altura: "))
print("Ingrese las dimensiones del segundo rectángulo:")
base2 = float(input("Base: "))
altura2 = float(input("Altura: "))

# Crear instancias de Rectangulo
rectangulo1 = Rectangulo(base1, altura1)
rectangulo2 = Rectangulo(base2, altura2)
# Comparar los rectángulos
print("")
print("Comparando rectángulos...")
print(f"¿Son iguales? {rectangulo1 == rectangulo2}")
print(f"¿Son diferentes? {rectangulo1 != rectangulo2}")
print(f"¿El primer rectángulo es mayor que el segundo? {rectangulo1 > rectangulo2}")
print(f"¿El primer rectángulo es menor que el segundo? {rectangulo1 < rectangulo2}")

input("Presione ENTER para continuar...")
import os
os.system('clear')
###########
#Implemente una clase Playlist que tenga una lista de sus canciones favoritas.
#Use el método __len__ para devolver el número de canciones mediante el llamado
#len(miLista). Utilice además el método __getitem__ para devolver una can-
#ción de la lista de acuerdo al argumento recibido en el método. Finalmente utilice
#__setitem__ para establecer una nueva canción en la posición indicada, ambos
#pasados como argumentos del método.

#class Playlist:
#Método constructor
class Playlist:

#Inicializar la lista de canciones
    def __init__(self):
        self.canciones = {
            0: {'nombre': 'Yesterday', 'artista': 'The Beatles', 'letra': 'Yesterday, all my troubles seemed so far away...'},
            1: {'nombre': 'Bohemian Rhapsody', 'artista': 'Queen', 'letra': 'Is this the real life? Is this just fantasy? Caught in a landslide...'},
            2: {'nombre': 'Ya lo pasado pasado', 'artista': 'Jose Jose', 'letra': 'Ya lo pasado, pasado...'},
            3: {'nombre': 'La bilirrubina', 'artista': 'Juan Luis Guerra', 'letra': 'Me sube por la cabeza y me baja por los pies...'},
            4: {'nombre': 'Despacito', 'artista': 'Luis Fonsi', 'letra': 'Despacito, quiero respirar tu cuello despacito...'}   
        } #Inicializando dicionario con canciones
        self.contador_canciones = len(self.canciones) #Inicializar la llave

    #Método para agregar una canción
    def agregar_cancion(self, cancion):
        self.canciones[self.contador_canciones] = cancion #Usando el contador como clave
        self.contador_canciones += 1
        print(f"Se ha agregado la canción: {cancion['nombre']} de {cancion['artista']}")
        return cancion

    #Método para obtener el número de canciones
    def __len__(self):
        return len(self.canciones)

    #Método para obtener una canción por su índice
    def __getitem__(self, key):
        return self.canciones[key]

    #Método para establecer una canción en una posición específica
    def __setitem__(self, key, cancion):
        self.canciones[key] = cancion

#Menu Principal
#inicializar la playlist
mi_playlist = Playlist()
#Ciclo principal del menú
while True:
    ##Mostrar mensaje de bienvenida
    print ("")
    print ("")
    print ("Bienvenido a la Playlist de Canciones")
    print ("-----Menu Principal-----")
    ##Mostrar opciones del menú
    print ("")
    print ('Seleccione su opción:')
    print ('1. Agregar Canción')
    print ('2. Consultar numero de canciones existentes')
    print ('3. Listar Canciones')
    print ('4. Consultar Canción (Nombre, Artista, Letra)')
    print ('5. Modificar Canción')
    print ('6. Salir')
    print ("")
    
    opcion=input("Ingrese su opción: ")

    if opcion == '1':
        nombre_cancion=str(input("Introduzca el nombre de la canción: "))
        nombre_artista=str(input("Introduzca el nombre del artista: "))
        letra_cancion = str(input("Introduzca la letra de la canción: "))

        nueva_cancion = {
            'nombre': nombre_cancion,
            'artista': nombre_artista,
            'letra': letra_cancion
        }
        #Llamar al método para agregar la canción
        mi_playlist.agregar_cancion(nueva_cancion)
        print(f"se ha agregado la canción: {nueva_cancion}")
        input("Presione ENTER para continuar...")
        import os
        os.system('clear')

    elif opcion == '2':
        # Llamar al método consultar_cancion que ya creamos
        print(f"Total de canciones en la playlist: {len(mi_playlist)}")
        input("Presione ENTER para continuar...")
        import os
        os.system('clear')
                
    elif opcion == '3':
        print("Listar Canciones")
        # Llamar al método para listar las canciones
        for key, cancion in mi_playlist.canciones.items():
            print(f"{key+1}: {cancion['nombre']} - {cancion['artista']}")
        input("Presione ENTER para continuar...")
        import os
        os.system('clear')
    elif opcion == '4':
        print("Consultar Canción")
        # Llamar al método para para listar las canciones        
        indice = int(input("Ingrese el número de la canción que desea consultar: ")) - 1
        if 0 <= indice < len(mi_playlist):
            cancion = mi_playlist[indice]
            print(f"Canción: {cancion['nombre']}\nArtista: {cancion['artista']}\nLetra:\n{cancion['letra']}")
        else:
            print("Número de canción inválido.")
        input("Presione ENTER para continuar...")
        import os
        os.system('clear')
    elif opcion == '5': #Usar __setitem__ para establecer una nueva canción
        indice = int(input("Ingrese el número de la canción que desea modificar: ")) - 1
        if 0 <= indice < len(mi_playlist):
            nombre_cancion = str(input("Introduzca el nuevo nombre de la canción: "))
            nombre_artista = str(input("Introduzca el nuevo nombre del artista: "))
            letra_cancion = str(input("Introduzca la nueva letra de la canción: "))

            nueva_cancion = {
                'nombre': nombre_cancion,
                'artista': nombre_artista,
                'letra': letra_cancion
            }
            mi_playlist[indice] = nueva_cancion
            print(f"Se ha actualizado la canción en la posición {indice + 1}.")
        else:
            print("Número de canción inválido.")
        input("Presione ENTER para continuar...")
        import os
        os.system('clear')

    elif opcion == '6':
        print("Saliendo de la Playlist")
        break
    