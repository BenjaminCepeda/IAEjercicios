import math


# Función que calcula el área del círculo
def areaCirculo(r):
    return math.pi * r ** 2


# Función que calcula el volúmen de un cilindro
def volumenCirculo(r, h):
    return areaCirculo(r) * h


print("\t CALCULO DE AREA DE CIRCULO ")
radio = float(input("Ingrese el radio del círculo:"))
print("El área del circulo con radio:{:.6f} es: {:.6f}".format(radio, areaCirculo(radio)))

print("\n\t CALCULO DEL VOLUMEN DE UN CILINDRO")
radio = float(input("Ingrese el radio del cilindro:"))
altura = float(input("Ingrese la altura del cilindro:"))
print("El volúmen del cilindro con radio: {:.6f} y altura: {:.6f} es:{:.6f}".format(radio, altura, volumenCirculo(radio, altura)))
