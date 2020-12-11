"""
文件说明

"""
import sympy

sympy.init_printing()
x, y = sympy.symbols('x y')
print(sympy.sqrt(x**2 + y**2))

x = 2
y = 2
print((sympy.sqrt(x**2 + y**2))**2)

a = 5
b = -6
print(a+b)

print((-1, 0, -3)[1])