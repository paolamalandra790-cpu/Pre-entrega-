import requests

BASE_URL = "https://reqres.in/api"

def get_users(page=1):
    return requests.get(f"{BASE_URL}/users?page={page}")

def login(email, password=None):
    datos = {"email": email}
    if password:
        datos["password"] = password
    return requests.post(f"{BASE_URL}/login", json=datos)

def create_user(nombre, trabajo):
    return requests.post(f"{BASE_URL}/users", json={"name": nombre, "job": trabajo})
