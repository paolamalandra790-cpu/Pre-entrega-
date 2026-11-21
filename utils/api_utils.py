import requests

BASE_URL = "https://fakestoreapi.com"

def get_productos():
    """Trae la lista de productos desde la API"""
    respuesta = requests.get(f"{BASE_URL}/products", timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()

def get_producto_por_id(producto_id):
    """Trae un producto por su id"""
    respuesta = requests.get(f"{BASE_URL}/products/{producto_id}", timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()

def crear_producto(datos_producto):
    """Crea un producto nuevo en la API"""
    respuesta = requests.post(f"{BASE_URL}/products", json=datos_producto, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()
