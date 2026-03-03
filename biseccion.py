# Laboratorio de Bisección - Sesión 02
# Proyecto: EcoCity Manager

class AnalizadorMatematico:
    def __init__(self, funcion, tolerancia=1e-5):
        self.f = funcion
        self.tol = tolerancia

    def encontrar_raiz(self, a, b):
        """Implementa el algoritmo de bisección paso a paso."""
        
        # 1. Validación inicial (Teorema de Bolzano)
        if self.f(a) * self.f(b) >= 0:
            print("❌ Error: Los signos en los extremos deben ser opuestos.")
            return None

        # 2. Proceso iterativo
        intentos = 0
        while (b - a) / 2 > self.tol:
            intentos += 1
            punto_medio = (a + b) / 2
            
            # Si tocamos la raíz exacta, salimos
            if self.f(punto_medio) == 0:
                break
            
            # Reasignamos límites según el cambio de signo
            if self.f(a) * self.f(punto_medio) < 0:
                b = punto_medio
            else:
                a = punto_medio
        
        print(f"✅ Convergencia lograda en {intentos} iteraciones.")
        return (a + b) / 2

# --- PRUEBA DE CAMPO ---
if __name__ == "__main__":
    # Queremos saber dónde x^2 - 9 es cero (esperamos un 3)
    mi_funcion = lambda x: x**2 - 9
    
    simulador = AnalizadorMatematico(mi_funcion)
    resultado = simulador.encontrar_raiz(0, 5)
    
    print(f"📍 La raíz aproximada es: {resultado}")