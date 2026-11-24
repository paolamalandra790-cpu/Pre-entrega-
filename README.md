# Pre-Entrega - Automatización QA

Proyecto de automatización de pruebas para la Entrega Final del curso de QA.

## Objetivo
Automatizar el flujo de login y compra de la tienda SauceDemo usando Selenium WebDriver con patrón Page Object Model (POM).

## Tecnologías
- Python
- Selenium WebDriver
- Pytest
- GitHub Actions (CI)

## Estructura del proyecto
- `pages/` - Page Objects (LoginPage, InventoryPage, CartPage)
- `tests_api/` - Tests de API
- `tests/` - Tests UI con Selenium
- `datos/` - Datos de prueba (JSON)
- `.github/workflows/` - Pipeline de CI que corre los tests en cada push

## Cómo ejecutar los tests
```bash
pip install -r requirements.txt
pytest
