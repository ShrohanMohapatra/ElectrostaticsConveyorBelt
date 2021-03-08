from sympy import *
m, n = symbols('m n',integers=True,nonnegative=True)
t = symbols('t')
print(integrate(sin(2*m*t)*sin(2*n*t),(t,0,pi/2)))
print(integrate(cos(2*m*t)*cos(2*n*t),(t,0,pi/2)))