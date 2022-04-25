"""
#Listas

s = [1, 1+1, 6/2, 3/8]
print(s)
print(s[3])
M = [[1, 2, 3], [4, 5, 6]]
print(M)
for f in range(len(M)):
    for c in range(len(M[0])):
        print(M[f][c])
# TUPLA

# FUNCIONES


def suma(a, b):
    return a+b


a = int(input("ingrese el 1er numero:"))
b = int(input("ingrese el 2do numero:"))
print("El resultado de la suma es: ", suma(a, b))


def resMultiple(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto


x, y = resMultiple(8,4)
print("El resultado es: ", resMultiple(8,4))
print("El resultado es: ", x, y)

"""
import statistics


class Calculo:
    def __init__(self, lista, intervalo):
        self.lista = lista
        self.intervalo = intervalo

    def agrupar(self):
        return statistics.median_grouped(self.lista, self.intervalo)

    def toStr(self):
        propiedades = ("lista: {}, intervalo: {}")
        print(self.lista)
        print(self.intervalo)
        print(propiedades.format(self.lista, self.intervalo))


datos = [1, 2, 2, 2,3,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6]
interv = 2

Agrupamiento = Calculo(datos, interv)
mensaje = ("El agrupamiento de: {} con intervalo: {}, es:{}")
print ("El objeto creado es:", Agrupamiento.toStr())
print(mensaje.format(datos, interv, Agrupamiento.agrupar()))
