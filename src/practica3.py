# Escriba una clase llamada vector que deberá tener dos propiedades x, y para almacenar
# la posición del vector en el plano cartesiano. Además debe tener un método que calcule
# la magnitud del vector, uno que determine el ángulo en radianes y otro método que
# determine el ángulo en grados. La clase debe utilizar la función str() para mostrar la
# representación del vector de la forma (x, y).

# La clase también debe utilizar la función add para la suma de vectores. Recuerde que
# la suma de dos vectores se hace por componentes x y por componentes y. La suma
# debe devolver el resultado como vector en la forma (x, y).

# Importar la librería math para cálculos matemáticos
import math as mt

# Definición de la clase Vector
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitud(self):
        return (self.x**2 + self.y**2)**0.5

    def angulo_radianes(self):
        return mt.atan2(self.y, self.x)

    def angulo_grados(self):
        return mt.degrees(self.angulo_radianes())

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, otro_vector):
        # Sumar las componentes x e y de ambos vectores
        x_resultante = self.x + otro_vector.x
        y_resultante = self.y + otro_vector.y
        # Devolver un nuevo vector con las componentes resultantes
        return Vector(x_resultante, y_resultante)

# Introducción del programa
print("")
print("A continuación introduzca el número de vectores que desea sumar")
# Solicitar el número de vectores al usuario
print("")
n = int(input("Número de vectores: "))
# Inicializar la lista de vectores
vectores = []
# Bucle para solicitar las coordenadas de cada vector
for i in range(n):
    print("")
    print(f"Ingrese las coordenadas del vector {i + 1}:")
    print("")
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    # Crear un objeto Vector
    vector = Vector(x, y)
    # Calcular y mostrar la magnitud
    print("")
    print(f"El vector es: {vector}")
    print(f"    Su magnitud es: {vector.magnitud()}")
    print(f"    El ángulo en grados es: {vector.angulo_grados()}")
   
    # Agregar el objeto Vector a la lista
    vectores.append(vector)

# Sumar todos los vectores usando la función add
vector_resultante = vectores[0]
for vector in vectores[1:]:
    vector_resultante = vector_resultante.add(vector)

# Mostrar el resultado
print("")
print(f"La suma de los vectores {[str(v) for v in vectores]} es: {vector_resultante}")
print("")