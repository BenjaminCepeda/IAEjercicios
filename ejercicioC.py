import math

"""
Función que calcula el factorial de un número entero
"""


def calculaFactorial(n):
    return math.factorial(n)


print("\n\tFACTORIAL DE UN NUMERO ENTERO")
n = 0
try:  # Valida ingreso de numero entero positivo
    n = int(input("Ingrese un numero entero positivo: "))
    print("El factorial de n={} es {}".format(n, calculaFactorial(n)))
except ValueError: # Mensaje de error cuando el numero no es entero positivo
    print("Se ha ingresa un número inválido {}".format(n))
