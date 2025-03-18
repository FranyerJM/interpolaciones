import matplotlib.pyplot as plt

class InterpolacionTaylor():
    def __init__(self, datos={}, punto_de_interpolacion=0, orden=0):
        self.datos = datos
        self.punto = punto_de_interpolacion
        self.orden = orden
        
        self.valores = list(self.datos.values())
        self.fechas = list(self.datos.keys())
        self.derivada = 0.0
    
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
        
    def calcular_derivadas(self, orden):
        a = self.punto
        f = self.valores
        
        if orden == 1:
            derivada = (f[a] - f[a-1])
        elif orden == 2:
            derivada = (f[a] - 2*f[a-1] + f[a-2])
        elif orden == 3:
            derivada = (f[a] - 3*f[a-1] + 3*f[a-2] - f[a-3])
        else:
            print('Orden no valido, solo orden 1, 2, 3') 
            
        print(f'der:{derivada} y orden : {orden}')
            
        return derivada
            
    
    def polinomio_taylor(self, x):
        a = self.punto
        f = self.valores
        polinomio = 0
        if x < len(f):
            termino1 = f[a]
            termino2 = (self.calcular_derivadas(1) * (x - a))
            termino3 = (self.calcular_derivadas(2) / self.factorial(2)) * ( (x - a)**2 )
            termino4 = (self.calcular_derivadas(3) / self.factorial(3)) * ( (x - a)**3 )
            
            polinomio = termino1 + termino2 + termino3 + termino4
            print(f'Polinomio de taylor: {polinomio}')
            return polinomio
        else:
            print("x excedido")
            
    def resultados(self):
        x_valores = self.fechas
        y_valores = []
    
        # for i in range(self.punto - 2, self.punto + 3):
        #     if i >= 0 and i < len(x_valores):
        #         y_valor = self.polinomio_taylor(i)
        #         y_valores.append(y_valor)
        print(f'valores: {self.valores}')
        for x in self.valores:
            y_valor = (self.polinomio_taylor(x)*-1)/100
            y_valores.append(y_valor)
        
            
        print(f'y_valores: {y_valores}')
        return x_valores, y_valores.reverse()

    
    def graficar(self):
        x_valores, y_valores = self.resultados()
        y_original = self.valores

        plt.figure(figsize=(10, 6))
        plt.plot(x_valores, y_original, 'bo--', label='Datos Originales')
        plt.plot(x_valores[:len(y_valores)], y_valores, 'r--', label='Interpolación de Taylor')  # Ajuste del rango
        plt.ylabel('Valores')
        plt.xlabel('Fechas')
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
    
taylor = InterpolacionTaylor(datos=datos, punto_de_interpolacion=8, orden=3)


taylor.graficar()

