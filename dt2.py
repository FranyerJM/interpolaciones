from datetime import datetime, timedelta
from random import randint
import csv

class GenerarDatosClima():
    def __init__(self, dias):
        self.dias = dias
        self.fechas = []
        self.temperaturas = []
        self.datos = {}
        self.datos_export = []
        
    def generar_fechas(self):
        fecha_de_hoy = datetime.now()
        for i in range(self.dias):
            dia = fecha_de_hoy - timedelta(days=i)
            self.fechas.append(dia.date().strftime('%d/%m/%Y'))
        return self.fechas
            
            
    def generar_temperaturas(self):
        self.temperaturas = [randint(8, 35) for _ in range(self.dias)]
        return self.temperaturas
    
    def concatenar(self):
        for i in range(self.dias):
            self.datos[f'{self.fechas[i]}'] = self.temperaturas[i]
            
        self.datos_export = [{'Fecha': fecha, 'Temperatura':temperatura} for fecha, temperatura in self.datos.items()]
        return self.datos
                           
    def exportar_csv(self):
        with open('datos_temperaturas.csv', 'w', newline='') as archivo_csv:
            campos = ['Fecha', 'Temperatura']
            
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(self.datos_export)
            

datos = GenerarDatosClima(30)

datos.generar_fechas()
datos.generar_temperaturas()
datos.concatenar()
datos.exportar_csv()