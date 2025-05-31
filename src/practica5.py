#Práctica 5 - progrqmación funcional

#1. Dada una lista de números enteros cualquiera, utilice los métodos map, filter y reduce
#para filtrar los números impares de la lista y calcular la suma de sus cuadrados.

from functools import reduce

import os
os.system('clear')
# Uso
print("1. Dada una lista de números enteros cualquiera, utilice los métodos map, filter y reduce")
print("   para filtrar los números impares de la lista y calcular la suma de sus cuadrados.")
print("")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Números en la lista: {numeros}")
# Filtrar los números impares
num_filt_imp=list(filter(lambda x: x % 2 != 0, numeros))
print(f"Números impares en la lista: {num_filt_imp}")
# Calcular la suma de los cuadrados de los números impares
cuadrados = list(map(lambda x:x**2, num_filt_imp))
print(f"Cuadrados de los números impares: {(cuadrados)}")
# Reducir a la suma de cuadrados
suma = reduce(lambda x, y: x + y, cuadrados)
print(f"Suma de los cuadrados de los números impares: {suma}")
input("Presione ENTER para continuar...")
import os
os.system('clear')

#2. Dada una lista de diccionarios que representan productos con nombre (llave en el
#diccionario) y precio (valor de la llave en el diccionario), filtre los productos que
#cuestan más de $200, y aplique un descuento del 10%. Finalmente calcule el total de los
#productos que tienen descuento.

from functools import reduce

import os
os.system('clear')
# Uso
print("2. Dada una lista de diccionarios que representan productos con nombre (llave en el")
print("diccionario) y precio (valor de la llave en el diccionario), filtre los productos que")
print("cuestan más de $200, y aplique un descuento del 10%. Finalmente calcule el total de los")
print("productos que tienen descuento.")
print("")
productos = {"Arroz": 150, "Frijol": 250, "Aceite":300, "Azúcar": 180, "Sal": 50}
print(f"Productos canasta básica: {productos}")
# Filtrar productos que cuestan más de $200
productos_filtrados = list(filter(lambda item: item[1] > 200, productos.items()))
print(f"Productos que cuestan más de $200: {productos_filtrados}")
# Aplicar un descuento del 10%
productos_descuento = list(map(lambda item: (item[0], item[1] * 0.9), productos_filtrados))
print(f"Productos con descuento del 10%: {productos_descuento}")
# Calcular el total de los productos con descuento
total_descuento = reduce(lambda acc, item: acc + item[1], productos_descuento, 0)
print(f"Total de productos con descuento: {total_descuento}")
#
input("Presione ENTER para continuar...")
import os
os.system('clear')

#Existe un método llamado mínimos cuadrados que en su caso lineal permite obtener
#una línea recta que se aproxima a una serie de m puntos (x, y). La recta resultante
#del método es y = a0 + a1 x, y para calcular los coeficientes a0 y a1. UTilizar map, filter, reduce y lambda.

datos= [(1, 1.3), (2, 3.5), (3, 4.2), (4, 5), (5, 7), (6, 8.8), (7, 10.1), (8, 12.5), (9, 13), (10, 15.6)]
import os
os.system('clear')
# Uso
print("3. Existe un método llamado mínimos cuadrados que en su caso lineal permite obtener")
print("   una línea recta que se aproxima a una serie de m puntos (x, y). La recta resultante")
print("   del método es y = a0 + a1 x, y para calcular los coeficientes a0 y a1. Utilizar map,")
print("   filter, reduce y lambda.")
print("")
print(f"Datos: {datos}")
# Calcular la suma de x, y, x^2, xy
suma_x = reduce(lambda acc, item: acc + item[0], datos, 0)
suma_y = reduce(lambda acc, item: acc + item[1], datos, 0)
suma_x2 = reduce(lambda acc, item: acc + item[0]**2, datos, 0)
suma_xy = reduce(lambda acc, item: acc + item[0] * item[1], datos, 0)
# Calcular el número de puntos
m = len(datos)
# Calcular a1 y a0
a1 = (m * suma_xy - suma_x * suma_y) / (m * suma_x2 - suma_x**2)
a0 = (suma_y - a1 * suma_x) / m
print(f"Coeficientes: a0 = {a0}, a1 = {a1}")
input("Presione ENTER para continuar...")
import os
os.system('clear')


