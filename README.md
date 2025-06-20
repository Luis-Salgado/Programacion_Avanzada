# Programacion_Avanzada
Carpeta dedicada a los trabajos de Programación avanzada de la MTII-Anahuac.
Las prácticas se encuentran en la rama "master", carpeta src

Las prácticas se detallan a cotinuación:
## Practica 2
En esta práctica se desarrolla un programa en Python con la función
np.random.randint(0, 101, (5, 4, 3))
para formar una matriz de números aleatorios con la biblioteca numpy (np)
Donde los argumentos de la función indican:
a) Es una matriz 5 x 4 x 3
b) Se rellena con números aleatorios de 0 a 100.

Posteriormente, se obtienen los valores minimos y máximos con la función y su ubicación
np.min
np.max

Y se obtienen los valores de la posición aplanando las 
np.argmin
np.argmax

y através ed la función 
np.unravel_index
Se obtiene su ubicación

## Practica 3 - Métodos __str__ y __add__
En esta práctica se desarrollan dos secciones de código, 
a) La primer sección donde # Escriba una clase llamada vector con dos propiedades x, y correspondientes a 
la posición del vector en el plano cartesiano. Se calcula la magnitud del vector, 
y el ángulo en radianes y otro método que determina el ángulo en grados.
En esta se suman los vectores a través de la función add para la suma de vectores.

b) La segunda donde se Desarrolla un mini-sistema para el registro de huespedes de un hotel. Se desarrolla una clase Persona que tenga los atributos nombre y edad. dSe muestra la información de la persona. Se tiene otra clase
llamada Huesped que se construya a partir de la clase Persona de manera que hereda
sus propiedades y métodos. Al final se incluyen funciones que calculan el saldo a la fecha de corte.

## Practica 4 - Métodos mágicos
En esta práctica se desarrollan dos secciones de código, 
a) En la primer sección se realiza la comparación de dos rectangulos utilizando los métodos mágicos __init__, __eq__, __ne__, __gt__ y __lt__. Se realiza la comparación de sus lados y se informa el resultado.

b) La segunda donde se Desarrolla un mini-sistema para la visualización de una playlist y adición de canciones. Se utilizan los métodos __init__, __len__, __getitem__ y __set__item__. Se desarrolla un diccionario que almacena las canciones y através de los métodos se realiza la visualización del contenido de la playlist y su actualización.

## Practica 5 - Programación Funcional
Desarrollo de tres ejercicios con las funciones map, filter, reduce y lambda
a) Dada una lista de números enteros cualquiera, utilice los métodos map, filter y reduce
para filtrar los números impares de la lista y calcular la suma de sus cuadrados.

b) Dada una lista de diccionarios que representan productos con nombre (llave en el
diccionario) y precio (valor de la llave en el diccionario), filtre los productos que
cuestan más de $200, y aplique un descuento del 10%. Finalmente calcule el total de los
productos que tienen descuento.

c) Existe un método llamado mínimos cuadrados que en su caso lineal permite obtener
una línea recta que se aproxima a una serie de m puntos (x, y). La recta resultante
del método es y = a0 + a1 x, y para calcular los coeficientes a0 y a1. Utilizar map, filter, reduce y lambda para resolverlo.

## Practica 6 - Listas por comprensión
Desarrollo de los siguientes ejercicios:
1. Dadas dos listas de números, por ejemplo [1, 2, 3] y [4, 5, 6], genera una
nueva lista que contenga el producto de los elementos correspondientes.

3. Dada una lista de diccionarios que representan personas con claves “nombre”, “edad” y
“ciudad”, genera una nueva lista de nombres de personas que tengan más de 30 años y vivan en
“Madrid”.
Ejemplo: Para la lista [{"nombre":
"Ana", "edad": 25, "ciudad":
"Madrid"}, {"nombre": "Juan", "edad": 35, "ciudad": "Madrid"},
{"nombre": "Luis", "edad": 32, "ciudad": "Barcelona"}], el resultado
debería ser [“Juan”].

5. Dada una lista de listas de números, utiliza una expresión generadora para calcular la
media de todos los números.
Ejemplo: Para la lista [[1, 2, 3], [4, 5], [6, 7, 8]], el resultado debería ser 4.5.

7. Utiliza una expresión generadora para calcular la varianza de una lista de números. La
varianza se calcula como la media de los cuadrados de las diferencias con la media.
Ejemplo: Para la lista [1, 2, 3, 4, 5], el resultado debería ser 2.0.
