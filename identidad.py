import copy

# --- 1. ABSTRACCIÓN: El molde de nuestra ciudad ---
class Recurso:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

def ejecutar_laboratorio():
    print("--- 🔬 LABORATORIO DE MEMORIA Y FLUJO: ECO-CITY --- \n")

    # --- 2. EXPERIMENTO: INTEGER INTERNING (Bajo el capó) ---
    # Python optimiza números pequeños (-5 a 256)
    num_a = 100
    num_b = 100
    num_c = 500
    num_d = 500

    print(f"[Interning] ¿Es 100 el mismo objeto físico? {num_a is num_b}") # True
    print(f"[Interning] ¿Es 500 el mismo objeto físico? {num_c is num_d}") # False
    print("-" * 50)

    # --- 3. CREACIÓN DEL FLUJO ORIGINAL ---
    presupuesto_real = [Recurso("Fondo Municipal", 1000000)]
    
    # --- 4. EL PELIGRO: COPIA SUPERFICIAL (Shallow Copy) ---
    # Esto solo copia la "dirección", no el objeto.
    simulacion_riesgosa = list(presupuesto_real)
    simulacion_riesgosa[0].cantidad = 0 

    print("⚠️  ALERTA: Se usó copia superficial en la simulación.")
    print(f"Presupuesto REAL después del desastre: ${presupuesto_real[0].cantidad}")
    print(f"¿Son el mismo objeto en memoria?: {presupuesto_real[0] is simulacion_riesgosa[0]}")
    print("-" * 50)

    # Restauramos el valor para el siguiente experimento
    presupuesto_real[0].cantidad = 1000000

    # --- 5. LA SOLUCIÓN: DEEP COPY (Abstracción de Flujo Segura) ---
    # Creamos un universo paralelo totalmente independiente.
    simulacion_segura = copy.deepcopy(presupuesto_real)
    simulacion_segura[0].cantidad = 0

    print("✅ ÉXITO: Se usó DEEP COPY.")
    print(f"Presupuesto REAL (Blindado): ${presupuesto_real[0].cantidad}")
    print(f"Presupuesto SIMULADO (Alterado): ${simulacion_segura[0].cantidad}")
    print(f"¿Son objetos distintos?: {presupuesto_real[0] is not simulacion_segura[0]}")
    print(f"\nID Real: {id(presupuesto_real[0])}")
    print(f"ID Seguro: {id(simulacion_segura[0])}")

if __name__ == "__main__":
    ejecutar_laboratorio()