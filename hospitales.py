import copy

# 1. Abstracción simple
class Hospital:
    def __init__(self, nombre, camas):
        self.nombre = nombre
        self.camas = camas

# 2. Creación del objeto original
central = Hospital("Hospital Central", 50)
ciudad_real = [central]

# 3. Deep Copy para la simulación de crisis
# Bajo el capó: Creamos un universo paralelo de memoria
simulacion_crisis = copy.deepcopy(ciudad_real)
simulacion_crisis[0].camas = 0 # En la crisis no hay camas

# 4. Verificación de Integridad
print(f"¿Ciudad real afectada?: {ciudad_real[0].camas} camas") # Debe decir 50
#print(f"¿Son objetos distintos?: {central is simulacion_crisis[0]}") # Debe decir False
print(f"¿Son objetos independientes en memoria?: {central is not simulacion_crisis[0]}")
