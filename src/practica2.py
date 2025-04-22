#1. Desarrolle un programa en Python que genere una arreglo NumPy tridimensional de tamaño 5×4×3 con
#valores aleatorios entre 0 y 100. Posteriormente el programa debe encontrar el elemento más pequeño
#y el màs grande e indicar la ubicación de dichos elementos dentro del arreglo. Imprima la matriz, los
#valores menor y mayor, asì como sus ubicaciones. Guarde su programa en un archivo con extensión .py.

import numpy as np

# Crear un array tridimensional de ejemplo con números aleatorios entre 0 y 100
array_3d_random = np.random.randint(0, 101, (5, 4, 3))

# Encontrar el valor más pequeño
valor_minimo = np.min(array_3d_random)

# Encontrar el valor más grande
valor_maximo = np.max(array_3d_random)

# Encontrar las ubicaciones de esos valores
indice_minimo = np.argmin(array_3d_random)
indice_maximo = np.argmax(array_3d_random)

ubicacion_minimo = tuple(int(i) for i in np.unravel_index(indice_minimo, array_3d_random.shape))
ubicacion_maximo = tuple(int(i) for i in np.unravel_index(indice_maximo, array_3d_random.shape))

print("Array:")
print(array_3d_random)
print(f"El valor más pequeño es {valor_minimo}, ubicado en la posición {ubicacion_minimo}")
print(f"El valor más grande es {valor_maximo}, ubicado en la posición {ubicacion_maximo}")