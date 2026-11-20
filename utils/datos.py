import csv
import os

def leer_datos_login():
    ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "login.csv")
    datos = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append((fila["usuario"], fila["clave"], fila["resultado_esperado"]))
    return datos
