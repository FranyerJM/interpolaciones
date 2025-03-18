import matplotlib.pyplot as plt
from dt2 import GenerarDatosClima

class InterpolacionTaylor:
    def __init__(self, datos={}, punto_de_interpolacion=0, espacio_entre_puntos=1, diferencias='adelante', orden=1):
        """
        Inicializa la clase InterpolacionTaylor.

        Parámetros:
            datos: dict - Fecha:Valor
            punto_de_interpolacion: int - Índice del punto de interpolación
            espacio_entre_puntos: int - Cantidad de días entre los puntos
            diferencias: str - 'adelante', 'centrada', 'atras'
            orden: int - Cantidad de derivadas a calcular
        """
        self.punto_de_interpolacion = punto_de_interpolacion
        self.datos = datos
        self.espacio_entre_puntos = espacio_entre_puntos
        self.diferencias = diferencias
        self.orden = orden

        # Convertir datos a listas
        self.fechas = list(datos.keys())
        self.valores = list(datos.values())
        self.derivadas = []

    def factorial(self, n):
        """Calcula el factorial de un número."""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def binomial(self, n, k):
        """Calcula el coeficiente binomial."""
        fact_n = self.factorial(n)
        fact_k = self.factorial(k)
        fact_n_k = self.factorial(n - k)
        return fact_n / (fact_k * fact_n_k)

    def calculo_adelante(self, orden_derivada):
        """Calcula la derivada utilizando diferencias hacia adelante."""
        f = self.valores
        a = self.punto_de_interpolacion
        h = self.espacio_entre_puntos

        suma = 0.0
        for k in range(orden_derivada + 1):
            coeficiente = (-1) ** k * self.binomial(orden_derivada, k)
            valor_funcion = f[a + (orden_derivada - k)]
            suma += coeficiente * valor_funcion
        return suma / (h ** orden_derivada)

    def calculo_atras(self, orden_derivada):
        """Calcula la derivada utilizando diferencias hacia atrás."""
        f = self.valores
        a = self.punto_de_interpolacion
        h = self.espacio_entre_puntos

        suma = 0.0
        for k in range(orden_derivada + 1):
            coeficiente = (-1) ** k * self.binomial(orden_derivada, k)
            valor_funcion = f[a - k]
            suma += coeficiente * valor_funcion
        return suma / (h ** orden_derivada)

    def calculo_central(self, orden_derivada):
        """Calcula la derivada utilizando diferencias centradas."""
        f = self.valores
        a = self.punto_de_interpolacion
        h = self.espacio_entre_puntos

        suma = 0.0
        for k in range(-orden_derivada, orden_derivada + 1):
            if k != 0:
                coeficiente = (-1) ** k * self.binomial(2 * orden_derivada, orden_derivada + k)
                valor_funcion = f[a + k]
                suma += coeficiente * valor_funcion
        return suma / (2 * (h ** orden_derivada))

    def calcular_derivadas(self):
        """Calcula las derivadas según el tipo de diferencias especificado."""
        if self.diferencias.lower() == 'adelante':
            for i in range(1, self.orden + 1):
                derivada = self.calculo_adelante(i)
                self.derivadas.append(derivada)
        elif self.diferencias.lower() == 'centrada':
            for i in range(1, self.orden + 1):
                derivada = self.calculo_central(i)
                self.derivadas.append(derivada)
        elif self.diferencias.lower() == 'atras':
            for i in range(1, self.orden + 1):
                derivada = self.calculo_atras(i)
                self.derivadas.append(derivada)
        else:
            raise ValueError("Tipo de diferencias no válido.")

    def polinomio_taylor(self, x):
        """Calcula el polinomio de Taylor en un punto x."""
        a = self.punto_de_interpolacion
        f_a = self.valores[a]
        polinomio = f_a
        for i in range(1, self.orden + 1):
            polinomio += self.derivadas[i - 1] * (x - a) ** i / self.factorial(i)
        return polinomio

    def graficar(self):
        """Grafica los datos y el polinomio de Taylor."""
        x = range(len(self.fechas))
        y = self.valores
        y_taylor = [self.polinomio_taylor(i) for i in x]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'bo-', label='Datos originales')
        plt.plot(x, y_taylor, 'r--', label='Polinomio de Taylor')

        plt.axvline(x=self.punto_de_interpolacion, color='k', linestyle='--', label='Punto de interpolación')
        plt.xlabel('Fechas')
        plt.ylabel('Valores')
        plt.title('Interpolación de Taylor')
        plt.legend()
        plt.grid()
        plt.show()


# Datos de ejemplo
datos = GenerarDatosClima(30)
datos.generar_fechas()
datos.generar_temperaturas()
data = datos.concatenar()
print(data)

# Crear instancia de la clase
taylor = InterpolacionTaylor(data, punto_de_interpolacion=15, espacio_entre_puntos=1, diferencias='centrada', orden=5)

# Calcular derivadas
taylor.calcular_derivadas()

# Graficar resultados
taylor.graficar()
