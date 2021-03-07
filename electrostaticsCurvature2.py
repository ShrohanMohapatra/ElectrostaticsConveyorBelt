from sympy import *
fm, r, theta, R = symbols('fm r theta R',nonnegative = True)
m = symbols('m',integers=True,nonnegative=True)
r0, re, t, f1, f2 = symbols('r0 re t f1 f2')
f = fm*sin(2*m*theta)*(R/r)**(2*m)
print("Er = ",simplify(diff(-f,r)))
print("Et = ",simplify(1/r*diff(-f,theta)))
print(simplify(integrate(r**(-4*m-1),(r,r0,re))))
f = fm*sin(2*m*theta)*(r/R)**(2*m)
print("Er = ",simplify(diff(-f,r)))
print("Et = ",simplify(1/r*diff(-f,theta)))
print(simplify(integrate(r**(4*m-1),(r,r0,re))))
f = fm*sin(2*theta)*(r/R)**2
print("Er = ",simplify(diff(-f,r)))
print("Et = ",simplify(1/r*diff(-f,theta)))
print(simplify(integrate(cos(2*m*t)**2,(t,0,pi/2))))
print(simplify(integrate(sin(2*m*t)**2,(t,0,pi/2))))
print(simplify(integrate(m*pi/4/r*(f1**2)*(r/R)**(4*m),(r,r0,re))))
print(simplify(integrate(m*pi/4/r*(f2**2)*(R/r)**(4*m),(r,r0,re))))
