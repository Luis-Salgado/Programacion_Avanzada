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
    print(f"    El ángulo en radianes es: {vector.angulo_radianes()}")
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

###
#Desarrollar un mini-sistema para el registro de huespedes de un hotel. Para ello
#desarrolle una clase Persona que tenga los atributos nombre y edad. debe tener una
#propiedad que muestre la información de la persona. Desarrolle además otra clase
#llamada Huesped que se construya a partir de la clase Persona de manera que herede
#sus propiedades y métodos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def info_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Huesped(Persona):
    def __init__(self, nombre, edad, habitacion, rfc, numero_cuenta, fecha_ingreso, hospedado_actualmente=True):
        super().__init__(nombre, edad)
        self.habitacion = habitacion
        self.rfc = rfc
        self.numero_cuenta = numero_cuenta
        self.fecha_ingreso = fecha_ingreso
        self.hospedado_actualmente = hospedado_actualmente
        self.servicio_a_la_habitacion = {}
        self.tarifa_por_noche = 500.00  # Tarifa base por noche (podría ser variable)

    def mostrar_info_basica(self):
        print(f"--- Información del Huésped ---")
        print(f"Nombre: {self.nombre}")
        print(f"Habitación: {self.habitacion}")
        print(f"Fecha de Ingreso: {self.fecha_ingreso}")
        print(f"Hospedado Actualmente: {'Sí' if self.hospedado_actualmente else 'No'}")

    def agregar_servicio(self, producto, costo):
        self.servicio_a_la_habitacion[producto] = costo

    def calcular_saldo(self, fecha_actual):
        from datetime import datetime

        try:
            fecha_ingreso_dt = datetime.strptime(self.fecha_ingreso, '%Y-%m-%d')
            fecha_actual_dt = datetime.strptime(fecha_actual, '%Y-%m-%d')
            dias_hospedado = (fecha_actual_dt - fecha_ingreso_dt).days
        except ValueError:
            print("Error: Formato de fecha incorrecto (YYYY-MM-DD).")
            return None

        costo_habitacion = dias_hospedado * self.tarifa_por_noche
        costo_servicios = sum(self.servicio_a_la_habitacion.values())
        saldo_total = costo_habitacion + costo_servicios
        return saldo_total

# Ejemplo de uso
print ("Ahora pasará al mini-sistema de registro de huespedes del hotel")
print ("")
print ("¿Cuántos huespedes desea registrar?")
# Solicitar el número de huéspedes al usuario
n = int(input("Número de huéspedes: "))
# Inicializar la lista de huéspedes
huespedes = []
# Bucle para solicitar la información de cada huésped
for i in range(n):
    print("")
    print(f"Ingrese la información del huésped {i + 1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    habitacion = int(input("Número de habitación: "))
    rfc = input("RFC: ")
    numero_cuenta = float(input("Número de cuenta: "))
    fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ")
    hospedado_actualmente = input("¿Está hospedado actualmente? (Sí/No): ").strip().lower() == 'sí'

    # Crear un objeto Huesped
    huesped = Huesped(nombre, edad, habitacion, rfc, numero_cuenta, fecha_ingreso, hospedado_actualmente)
    huespedes.append(huesped)
    print(f"Información completa: {huesped.info_persona}, Habitación: {huesped.habitacion}, RFC: {huesped.rfc}, Cuenta: {huesped.numero_cuenta}, Ingreso: {huesped.fecha_ingreso}, ¿Hospedado?: {huesped.hospedado_actualmente}")

# Ejemplo de agregar servicios y calcular saldo

print('desea agregar servicios a los huespedes?')
respuesta = input("¿Si o No?: ").strip().lower()
if respuesta == 'si':
    for huesped in huespedes:
        print(f"\nAgregando servicios para {huesped.nombre}:")
        while True:
            servicio = input("Nombre del servicio (o 'salir' para terminar): ")
            if servicio.lower() == 'salir':
                break
            costo = float(input(f"Costo del servicio '{servicio}': "))
            huesped.agregar_servicio(servicio, costo)
        print(f"Servicios agregados para {huesped.nombre}: {huesped.servicio_a_la_habitacion}")
else:
    print("No se agregarán servicios.")
# Ejemplo de cálculo de saldo
print('desea agregar servicios a los huespedes?')
respuesta = input("¿Si o No?: ").strip().lower()
if respuesta == 'si':
    for huesped in huespedes:
        print(f"\nAgregando servicios para {huesped.nombre}:")
        while True:
            servicio = input("Nombre del servicio (o 'salir' para terminar): ")
            if servicio.lower() == 'salir':
                break
            costo = float(input(f"Costo del servicio '{servicio}': "))
            huesped.agregar_servicio(servicio, costo)
        print(f"Servicios agregados para {huesped.nombre}: {huesped.servicio_a_la_habitacion}")
        print(f"Saldo total para {huesped.nombre}: {huesped.calcular_saldo('today')}")
        
else:
    print("No se agregarán servicios.")

#Calcular saldo
print('desea calcular el saldo de los huespedes?')
respuesta = input("¿Si o No?: ").strip().lower()
if respuesta == 'si':
    fecha_actual = input("Ingrese la fecha actual (YYYY-MM-DD): ")
    for huesped in huespedes:
        saldo = huesped.calcular_saldo(fecha_actual)
        if saldo is not None:
            print(f"Saldo total para {huesped.nombre}: {saldo}")
else:
    print("No se calculará el saldo.")
print("")
print("Fin del programa")
print("")
