import matplotlib.pyplot as plt

class InterpolacionTaylor:
    def __init__(self, datos={}, punto_de_interpolacion=0, orden=0):
        self.datos = datos
        self.punto = punto_de_interpolacion
        self.orden = orden
        
        self.valores = list(self.datos.values())
        self.fechas = list(self.datos.keys())
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
        
    def calcular_derivadas(self, orden):
        a = self.punto
        f = self.valores
        
        if orden == 1:
            return (f[a] - f[a-1])
        elif orden == 2:
            return (f[a] - 2*f[a-1] + f[a-2])
        elif orden == 3:
            return (f[a] - 3*f[a-1] + 3*f[a-2] - f[a-3])
        else:
            print('Orden no válido, solo orden 1, 2, 3') 
            return None
            
    def polinomio_taylor(self, x):
        a = self.punto
        f = self.valores
        
        if a < len(f) and x < len(f):
            polinomio = f[a]
            for n in range(1, self.orden + 1):
                derivada = self.calcular_derivadas(n)
                polinomio += (derivada / self.factorial(n)) * ((x - a) ** n)
            return polinomio
        else:
            print("x excedido")
            return None
            
    def resultados(self):
        x_valores = []
        y_valores = []
        y_original = []
    
        for i in range(self.punto - 3, self.punto + 4):
            if i in self.fechas:
                x_valores.append(i)
                y_original.append(self.valores[i])
                y_valor = self.polinomio_taylor(i)
                y_valores.append(y_valor)

        x_suave = [x + (i/10) for x in x_valores for i in range(1, 11)]
        y_suave = [self.polinomio_taylor(x) for x in x_suave]

        return x_valores, y_valores, y_original, x_suave, y_suave

    def graficar(self):
        x_valores, y_valores, y_original, x_suave, y_suave = self.resultados()

              
        plt.figure(figsize=(10, 6))
        plt.scatter(x_valores, y_original, label='Datos Originales')
        plt.plot(x_suave, y_suave, 'r-', linewidth=2, label='Interpolación suavizada')
        plt.ylabel('Valores')
        plt.xlabel('Dias')
        plt.title('Interpolación de Taylor')
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
    
taylor = InterpolacionTaylor(datos=datos, punto_de_interpolacion=3, orden=3)
taylor.graficar()
