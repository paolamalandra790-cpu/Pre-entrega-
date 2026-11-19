from faker import Faker

fake = Faker()

def test_generar_datos_falsos_con_faker():
    nombre = fake.first_name()
    apellido = fake.last_name()
    email = fake.email()
    password = fake.password()

    print(f"Nombre: {nombre} {apellido}")
    print(f"Email: {email}")
    print(f"Password: {password}")

    assert "@" in email
    assert len(nombre) > 0
    assert len(password) > 0

def test_generar_usuario_para_login():
    usuario = fake.user_name()
    clave = "secret_sauce"

    print(f"Usuario generado: {usuario}")

    assert len(usuario) > 0
    assert clave == "secret_sauce"
