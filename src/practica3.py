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
    
huesped1 = Huesped("Ana Pérez", 35, 101, "APE350715XX9", 1234567890.12, "2025-05-01")
huesped1.mostrar_info_basica()
print(f"Información completa: {huesped1.info_persona}, Habitación: {huesped1.habitacion}, RFC: {huesped1.rfc}, Cuenta: {huesped1.numero_cuenta}, Ingreso: {huesped1.fecha_ingreso}, ¿Hospedado?: {huesped1.hospedado_actualmente}")

huesped1.agregar_servicio("Desayuno", 80.00)
huesped1.agregar_servicio("Lavandería", 120.50)

saldo_hoy = huesped1.calcular_saldo("2025-05-03")
if saldo_hoy is not None:
    print(f"\nSaldo hasta el 2025-05-03: ${saldo_hoy:.2f}")

huesped2 = Huesped("Carlos López", 28, 205, "CLO280120YY7", 9876543210.55, "2025-04-28", False)
huesped2.mostrar_info_basica()
print(f"Información completa: {huesped2.info_persona}, Habitación: {huesped2.habitacion}, RFC: {huesped2.rfc}, Cuenta: {huesped2.numero_cuenta}, Ingreso: {huesped2.fecha_ingreso}, ¿Hospedado?: {huesped2.hospedado_actualmente}")

saldo_ayer = huesped2.calcular_saldo("2025-04-30")
if saldo_ayer is not None:
    print(f"\nSaldo hasta el 2025-04-30 para {huesped2.nombre}: ${saldo_ayer:.2f}")