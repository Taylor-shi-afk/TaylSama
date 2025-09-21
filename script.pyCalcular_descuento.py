def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el monto total y un porcentaje.

    Args:
      monto_total (float): El costo total de la compra.
      porcentaje_descuento (float): El porcentaje de descuento a aplicar. Por defecto es 10.

    Returns:
      float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
print("--- Calculadora de Descuentos ---")

# Primera llamada: solo se ingresa el monto total, se usa el descuento por 10%
monto_1 = float(input("Ingrese el monto total de la primera compra: "))
descuento_1 = calcular_descuento(monto_1)
precio_final_1 = monto_1 - descuento_1
print(f"Monto de la primera compra: ${monto_1:.2f}")
print(f"Descuento aplicado (10%): ${descuento_1:.2f}")
print(f"Monto final a pagar: ${precio_final_1:.2f}\n")

# Segunda llamada: se ingresa el monto total y un porcentaje de descuento personalizado
monto_2 = float(input("Ingrese el monto total de la segunda compra: "))
porcentaje_2 = float(input("Ingrese el porcentaje de descuento a aplicar: "))
descuento_2 = calcular_descuento(monto_2, porcentaje_2)
precio_final_2 = monto_2 - descuento_2
print(f"\nMonto de la segunda compra: ${monto_2:.2f}")
print(f"Descuento aplicado ({porcentaje_2}%): ${descuento_2:.2f}")
print(f"Monto final a pagar: ${precio_final_2:.2f}")