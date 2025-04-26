# Escriba una clase llamada vector que deberá tener dos propiedades x, y para almacenar
# la posición del vector en el plano cartesiano. Además debe tener un método que calcule
# la magnitud del vector, uno que determine el ángulo en radianes y otro método que
# determine el ángulo en grados. La clase debe utilizar la función str() para mostrar la
# representación del vector de la forma (x, y).

# La clase también debe utilizar la función add para la suma de vectores. Recuerde que
# la suma de dos vectores se hace por componentes x y por componentes y. La suma
# debe devolver el resultado como vector en la forma (x, y).

import math as mt

# Definición de la clase Vector
def vector(x, y):
    # Calcular la magnitud del vector
    magnitud = (x**2 + y**2)**0.5
    # Calcular el ángulo en radianes
    angulo_radianes = mt.atan2(y, x)
    # Calcular el ángulo en grados
    angulo_grados = mt.degrees(angulo_radianes)
    # Devolver las coordenadas y propiedades del vector
    return (x, y, magnitud, angulo_radianes, angulo_grados)

# Solicitar las coordenadas del vector al usuario
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

# Llamar a la función vector con los valores ingresados
x, y, magnitud, angulo_radianes, angulo_grados = vector(x, y)

# Mostrar los resultados
print(f"Vector: ({x}, {y})")
print(f"Magnitud: {magnitud}")
print(f"Ángulo en radianes: {angulo_radianes}")
print(f"Ángulo en grados: {angulo_grados}")
print("Las coordenadas del vector son:", (x, y))