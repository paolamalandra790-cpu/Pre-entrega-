# language: es
@ui @regression
Feature: Funcionalidad del carrito

  Background:
    Given que estoy logueado con el usuario "standard_user"

  Scenario: Agregar "Sauce Labs Backpack" al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito debería ser "1"

  Scenario: Agregar múltiples productos al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    And agrego el producto "Sauce Labs Bike Light" al carrito
    Then el contador del carrito debería ser "2"
