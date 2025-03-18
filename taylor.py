import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Cargar los datos
datos = pd.read_csv('temperaturas_semanales.csv')

# Asegurarse de que la columna de fechas sea del tipo datetime
datos['Fecha'] = pd.to_datetime(datos['Fecha'])

# Extraer temperaturas y días
x = np.arange(len(datos))
y = datos['Temperatura'].values

# Elegir el punto de interpolación (por ejemplo, el tercer día)
a = 2  # Tercer día (índice 2)

# Calcular derivadas
f_a = y[a]
f_prime_a = (y[a + 1] - y[a - 1]) / 2  # Aproximación de la primera derivada
f_double_prime_a = y[a + 1] - 2 * y[a] + y[a - 1]  # Aproximación de la segunda derivada

# Interpolación de Taylor de grado 2
def taylor_interpolation(x, a, f_a, f_prime_a, f_double_prime_a):
    return f_a + f_prime_a * (x - a) + (f_double_prime_a / math.factorial(a)) * (x - a) ** a

# Generar puntos para graficar
x_vals = np.linspace(0, len(datos) - 1, 100)
y_taylor = taylor_interpolation(x_vals, a, f_a, f_prime_a, f_double_prime_a)
print(y_taylor)
print(f'x: {x_vals}')

# Generar fechas correspondientes a x_vals
fechas_taylor_interp = pd.date_range(start='2023-03-01', periods=len(datos), freq='D')
fechas_taylor_interp = pd.date_range(start='2023-03-01', periods=100)

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(datos['Fecha'], y, 'o', label='Datos Originales')
plt.plot(fechas_taylor_interp, y_taylor, label='Interpolación de Taylor', color='orange')
plt.title('Interpolación de Taylor de Temperaturas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
