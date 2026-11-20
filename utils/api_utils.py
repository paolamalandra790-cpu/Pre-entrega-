import csv
import json

def leer_csv_login(ruta_archivo):
    """Lee el archivo CSV de credenciales de login. Retorna lista de tuplas para pytest.mark.parametrize"""
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        casos = []
        for fila in lector:
            debe = fila["debe_funcionar"].lower() == "true"
            casos.append((fila["usuario"], fila["clave"], debe, fila["descripcion"]))
        return casos

def leer_json_productos(ruta_archivo):
    """Lee el archivo JSON de productos. Retorna lista de productos para parametrizacion"""
    with open(ruta_archivo, encoding='utf-8') as archivo:
        return json.load(archivo)
