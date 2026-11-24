@ui @regresión
Característica: Funcionalidad del carrito

Fondo:
  Dado inicio sesión como "usuario_estándar" con la clave "salsa_secreta"

  Guión: Agregar "Mochila de Sauce Labs" al carrito
    Cuando agrego el producto "Mochila de Sauce Labs" al carrito
      Entonces el contador del carrito debe mostrar "1"

      Guión: Agregar múltiples productos al carrito
        Cuando agrego el producto "Mochila de Sauce Labs" al carrito
          Y agrego el producto "Luz para bicicleta de Sauce Labs" al carrito
            Entonces el contador del carrito debe mostrar "2"
