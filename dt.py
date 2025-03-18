import pandas as pd
import datetime
import numpy as np

# Generar fechas para una semana
fechas = pd.date_range(start='2023-03-01', periods=7)

# Generar temperaturas (simulando variación diaria)
temperaturas = 20 + 10 * np.sin(np.linspace(0, 2 * np.pi, 7))  # Temperaturas entre 10 y 30 grados

# Crear DataFrame
datos = pd.DataFrame({'Fecha': fechas, 'Temperatura': temperaturas})

# Guardar en un archivo CSV
datos.to_csv('temperaturas_semanales.csv', index=False)
