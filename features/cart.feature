@ui @regression
Feature: Funcionalidad del carrito

Background:
  Given inicio sesion como "standard_user" con la clave "secret_sauce"

  Scenario: Agregar "Sauce Labs Backpack" al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
      Then el contador del carrito debe mostrar "1"

      Scenario: Agregar multiples productos al carrito
        When agrego el producto "Sauce Labs Backpack" al carrito
          And agrego el producto "Sauce Labs Bike Light" al carrito
            Then el contador del carrito debe mostrar "2"
