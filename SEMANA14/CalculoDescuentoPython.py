#Crear una función para calcular el descuento del valor total de la compra.
def calcular_descuento(monto_total, porcentaje_descuento=0.1):
    descuento= porcentaje_descuento * monto_total #Calcular el descuento
    return descuento

#Llamar a la función por primera vez
compra_1=float(input("Ingrese el valor a pagar: "))
descuento_real=calcular_descuento(compra_1)
total_a_pagar=compra_1-descuento_real

#Imprimir resultados 1
print("Compra 1")
print(f"Monto subtotal a pagar: {compra_1:.2f}")
print(f"Descuento: {descuento_real:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")
print()

#Llamar a la función por segunda vez
compra_2=float(input("Ingrese el valor a pagar: "))
descuento_real= int(input("Ingrese valor de descuento: ")) * compra_2 / 100
total_a_pagar=compra_2-descuento_real

#Imprimir resultados 2
print("Compra 2")
print(f"Monto subtotal a pagar: {compra_2:.2f}")
print(f"Descuento: {descuento_real:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")