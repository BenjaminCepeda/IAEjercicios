from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S

# Imprimir en notacion matemática
printing.init_printing(use_latex='mathjax')
x = Symbol('x')  # Creando simbolo x
funcion = x**2 - x + 2
limit_expr = Limit(funcion, x, 2)  # Creando el objeto
print("El límite de {}".format(funcion))
print("Cuando x tiende a 2 es: {}".format(limit_expr.doit()))

#Resolviendo el limite 1/x cuando tiende a infinito
funcion = 1/x
limit_expr = limit(funcion, x, S.Infinity).doit()
print("El límite de {}".format(funcion))
print("Cuando x tiende a Infinito es: {}".format(limit_expr.doit()))
