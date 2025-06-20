#1. Ejercicio: Dadas dos listas de números, por ejemplo [1, 2, 3] y [4, 5, 6], genera una
#nueva lista que contenga el producto de los elementos correspondientes.

def producto_listas(lista1, lista2):
    producto=[x*y for x in lista1 for y in lista2]
    return producto
# Uso
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
import os
os.system('clear')
print("1. Dadas dos listas de números, por ejemplo [1, 2, 3] y [4, 5, 6], genera una")
print("nueva lista que contenga el producto de los elementos correspondientes.")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
resultado = producto_listas(lista1, lista2)
print(f"Producto de los elementos correspondientes: {resultado}")
input("Presione ENTER para continuar...")

os.system('clear')

#2. Dada una lista de diccionarios que representan personas con claves “nombre”, “edad” y “ciudad”,
#genera una nueva lista de nombres de personas que tengan más de 30 años y vivan en “Madrid”.
#Ejemplo: Para la lista [{"nombre": "Ana", "edad": 25, "ciudad":
#"Madrid"}, {"nombre": "Juan", "edad": 35, "ciudad": "Madrid"},
#{"nombre": "Luis", "edad": 32, "ciudad": "Barcelona"}], el resultado
#debería ser [“Juan”].

def filtrar_personas_madrid(personas):
    for persona in personas:
        if persona['edad'] > 30 and persona['ciudad'] == 'Madrid':
            yield persona['nombre']


# Uso
personas=[{"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
              {"nombre": "Juan", "edad": 35, "ciudad": "Madrid"},
              {"nombre": "Luis", "edad": 32, "ciudad": "Barcelona"}]
print("2. Dada una lista de diccionarios que representan personas con claves “nombre”, “edad” y “ciudad”,")
print("genera una nueva lista de nombres de personas que tengan más de 30 años y vivan en “Madrid”.")
print(f"Lista de personas: {personas}")
resultado = list(filtrar_personas_madrid(personas))
print(f"Nombres de personas mayores de 30 años que viven en Madrid: {resultado}")
input("Presione ENTER para continuar...")
import os
os.system('clear')

#3. Dada una lista de listas de números, utiliza una expresión generadora para calcular la
#media de todos los números.
#Ejemplo: Para la lista [[1, 2, 3], [4, 5], [6, 7, 8]], el resultado debería ser 4.5.

def calcular_media(lista_numeros):
    total = sum(num for sublista in lista_numeros for num in sublista)
    cantidad = sum(len(sublista) for sublista in lista_numeros)
    return total / cantidad if cantidad > 0 else 0
# Uso
lista_numeros = [[1, 2, 3], [4, 5], [6, 7, 8]]
print("3. Dada una lista de listas de números, utiliza una expresión generadora para calcular la")
print("media de todos los números.")
print(f"Lista de números: {lista_numeros}")
resultado = calcular_media(lista_numeros)
print(f"Media de todos los números: {resultado}")
input("Presione ENTER para continuar...")
import os
os.system('clear') 

#4. Utiliza una expresión generadora para calcular la varianza de una lista de números. La
#varianza se calcula como la media de los cuadrados de las diferencias con la media.
#Ejemplo: Para la lista [1, 2, 3, 4, 5], el resultado debería ser 2.0.

def calcular_varianza(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    varianza = sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)
    return varianza
# Uso
lista_numeros = [1, 2, 3, 4, 5]
print("4. Utiliza una expresión generadora para calcular la varianza de una lista de números.")
print("La varianza se calcula como la media de los cuadrados de las diferencias con la media.")
print(f"Lista de números: {lista_numeros}")
resultado = calcular_varianza(lista_numeros)
print(f"Varianza de la lista: {resultado}")
input("Presione ENTER para continuar...")
import os
os.system('clear')

