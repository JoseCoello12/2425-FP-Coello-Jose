def calcular_descuento(monto_total, porcentaje_descuento=30):
    descuento= (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 333.0
monto2= 545.5
porcentaje_descuento2 = 50

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)

# Calculo del valor total a cancelar
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"compra 1: Monto total: ${monto1:.2f}, Monto descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(f"compra 2: Monto total: ${monto2:.2f}, Monto descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")
