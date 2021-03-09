from sympy import *
r, d, R, t = symbols('r d R t')
m, bm, r0, rk = symbols('m bm r0 rk')
print(diff(-1/r*log(R**2/(r**2+d**2-2*d*r*cos(t))),t))
print(diff(-(cos(m*t)+bm*sin(m*t)),t))
print(diff(-log(R**2/(r**2+d**2-2*d*r*cos(t))),r))
print(diff(-1/m*(d/r)**m,r))
print(integrate(r*exp(-r0/r),(r,rk,oo)))