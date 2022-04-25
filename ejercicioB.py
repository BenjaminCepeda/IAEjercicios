"""
Función que calcula el total de una factura, sino se envía iva
utiliza por default 12 %
"""
def calculaTotalFactura(subTotal, iva=12.0):
    return subTotal + round(subTotal*iva/100, 2)
print("\tCALCULO DEL TOTAL DE UNA FACTURA")
print("\n\tCALCULO SOLICITANDO DOS PARÁMETROS")
subtotal = float(input("Ingrese el subtotal de la factura sin IVA:"))
iva = float(input("Ingrese el valir de IVA:"))
print("El valor total de la factura es: {:.2f}".format(calculaTotalFactura(subtotal, iva)))

print("\n\tCALCULO SIN SOLICITAR IVA")
subtotal = float(input("Ingrese el subtotal de la factura sin IVA:"))
print("El valor total de la factura es: {:.2f}".format(calculaTotalFactura(subtotal)))
