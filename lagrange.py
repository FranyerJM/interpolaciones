import matplotlib.pyplot as plt

class InterpolacionLagrange:
    def __init__(self, datos={}, cantidad_puntos=0):
        self.datos = datos
        self.fechas = list(self.datos.keys())
        self.valores = list(self.datos.values())
        self.fechas = self.fechas[:cantidad_puntos]
        self.valores = self.valores[:cantidad_puntos]
        
    def metodo_lagrange(self, x):
        polinomio = 0
        n = len(self.fechas)
        
        for i in range(n):
            termino = 1
            for j in range(n):
                if i != j:
                    termino *= (x - self.fechas[j]) / (self.fechas[i] - self.fechas[j])
            polinomio += termino * self.valores[i]
        return polinomio
    
    def resultados(self):
        min_x = min(self.fechas)
        max_x = max(self.fechas)
        paso = (max_x - min_x) / 100
        x_valores = [min_x + i*paso for i in range(101)] #  en este caso min_x es cero porque se agarran desde el inicio 0 hasta el index N
        
        y_valores = [self.metodo_lagrange(x) for x in x_valores]
        
        return x_valores, y_valores
    
    def graficar(self):
        x_v, y_v = self.resultados()
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.fechas, self.valores, label='Datos Originales', color='blue')
        plt.plot(x_v, y_v, 'r-', label='Interpolación de Lagrange')
        plt.ylabel('Valores')
        plt.xlabel('Fechas')
        plt.legend()
        plt.grid(True)
        plt.show()
        
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

lag = InterpolacionLagrange(datos=datos, cantidad_puntos=7)
lag.graficar()
