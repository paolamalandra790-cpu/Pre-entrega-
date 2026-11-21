@ui
Feature: Autenticación en SauceDemo
  Como usuario de SauceDemo
  Quiero iniciar sesión
  Para acceder al inventario de productos

  Background:
    Given que estoy en la página de login

  @smoke
  Scenario: Inicio de sesión exitoso con credenciales válidas
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And hago clic en el botón de login
    Then debería ser redirigido al inventario
    And debería ver el título "Products"

  @regression
  Scenario Outline: Inicio de sesión fallido
    When ingreso el usuario "<usuario>" y la contraseña "<password>"
    And hago clic en el botón de login
    Then debería ver el mensaje de error "<mensaje>"

    Examples:
      | usuario         | password       | mensaje                                                   |
      | invalid_user    | secret_sauce   | Epic sadface: Username and password do not match any user |
      | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.        |
      | standard_user   |                | Epic sadface: Password is required                          |
