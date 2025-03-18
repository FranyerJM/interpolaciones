import matplotlib.pyplot as plt
from math import factorial, comb

class InterpolacionTaylor:
    def __init__(self, datos={}):
        self.datos = datos
        self.temperaturas = list(datos.values())
        self.x_values = list(range(len(self.temperaturas)))
        self.x0 = None
        self.n = None
        self.coeficientes = []
        
    def configurar_interpolacion(self, orden):
        self.n = orden
        self.x0 = len(self.temperaturas) // 2
        if self.x0 + self.n >= len(self.temperaturas):
            raise ValueError(f"Datos insuficientes para orden {self.n}. Necesarios {self.x0 + self.n + 1} días")

    def calcular_derivada(self, k):
        suma = 0
        for j in range(k + 1):
            suma += ((-1) ** (k - j)) * comb(k, j) * self.temperaturas[self.x0 + j]
        return suma

    def generar_polinomio(self):
        self.coeficientes = []
        for k in range(self.n + 1):
            derivada = self.calcular_derivada(k)
            coef = derivada / factorial(k)
            self.coeficientes.append(coef)
            print(f"Orden {k}: derivada = {derivada:.2f}, coeficiente = {coef:.4f}")
    
    def polinomio_taylor(self, x):
        suma = 0
        for i in range(self.n + 1):
            suma += self.coeficientes[i] * (x - self.x0) ** i
        return suma
    
    def graficar(self):
        x_fino = [i / 10 for i in range(self.x_values[0] * 10, self.x_values[-1] * 10 + 1)]
        y_fino = [self.polinomio_taylor(x) for x in x_fino]

        plt.figure(figsize=(12, 5))
        plt.scatter(self.x_values, self.temperaturas, label="Datos originales", color="blue")
        plt.plot(x_fino, y_fino, "--", label=f"Taylor orden {self.n}", color="red")

        plt.xlabel("Día")
        plt.ylabel("Temperatura (°C)")
        plt.title("Interpolación de Taylor de Temperaturas Diarias")
        plt.legend()
        plt.grid(True)
        plt.show()

# Datos de ejemplo (puedes reemplazar esto con tus propios datos)
datos = {
    0: 21.9,
    1: 21.6,
    2: 21.9,
    3: 22.0,
    4: 22.3,
    5: 21.8,
    6: 20.9,
    7: 21.1,
    8: 21.6,
    9: 21.2,
    10: 21.7,
    11: 22.2,
    12: 22.3,
    13: 21.7,
    14: 22.3,
    15: 22.8,
    16: 24.0,
    17: 22.8,
    18: 22.8,
    19: 22.8,
    20: 24.4,
    21: 24.8,
    22: 23.7,
    23: 23.7,
    24: 23.4,
    25: 22.7,
    26: 22.7,
    27: 22.9,
    28: 23.1,
    29: 23.6,
    30: 22.4,
    31: 21.9,
}


# Crear instancia de la clase
taylor = InterpolacionTaylor(datos)

# Configurar la interpolación
orden = 1
taylor.configurar_interpolacion(orden)

# Generar el polinomio
taylor.generar_polinomio()

# Graficar resultados
taylor.graficar()
