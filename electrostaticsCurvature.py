from sympy import *
x, y = symbols('x y')
R = symbols('R',nonnegative=True)
fm = symbols('fm',nonnegative=True)
a = symbols('a',nonnegative=True)
h = symbols('h',nonnegative=True)
m = symbols('m',integer=True,nonnegative=True)
fZer = 2*fm*x*y*R**2/(x**2+y**2)**2
fInf = 2*fm*x*y/R**2
fSrc = fm*log(2*R**2/((x-R)**2+(y-R)**2))
fAcc = fm*((sqrt(x**2+y**2)/R)**m)*(cos(m*atan(y/x))+tan(m*pi/4)*sin(m*atan(y/x)))
print(diff(fZer,x).subs(x,a).subs(y,a))
print(diff(fZer,y).subs(x,a).subs(y,a))
print(diff(fInf,x).subs(x,a).subs(y,a))
print(diff(fInf,y).subs(x,a).subs(y,a))
init_printing()
print("Curvature for fZer = ",fZer)
print(
    simplify(abs((diff(fZer,y)**2*diff(fZer,x,2)-2*diff(fZer,x)*diff(fZer,y)
    *diff(fZer,x,y)+diff(fZer,x)**2*diff(fZer,y,2))/
    (diff(fZer,x)**2+diff(fZer,y)**2)**(3/2)).subs(x,a-h).subs(y,a+h))
)
print("Curvature for fInf = ",fInf)
print(
    simplify(abs((diff(fInf,y)**2*diff(fInf,x,2)-2*diff(fInf,x)*diff(fInf,y)
    *diff(fInf,x,y)+diff(fInf,x)**2*diff(fInf,y,2))/
    (diff(fInf,x)**2+diff(fInf,y)**2)**(3/2)).subs(x,a-h).subs(y,a+h))
)
print("Curvature for fSrc = ",fSrc)
print(
    simplify(abs((diff(fSrc,y)**2*diff(fSrc,x,2)-2*diff(fSrc,x)*diff(fSrc,y)
    *diff(fSrc,x,y)+diff(fSrc,x)**2*diff(fSrc,y,2))/
    (diff(fSrc,x)**2+diff(fSrc,y)**2)**(3/2)).subs(x,a).subs(y,a))
)
print(N(1/sqrt(2)))
print("Curvature for fAcc = ",fAcc)
print(
    simplify(abs((diff(fAcc,y)**2*diff(fAcc,x,2)-2*diff(fAcc,x)*diff(fAcc,y)
    *diff(fAcc,x,y)+diff(fAcc,x)**2*diff(fAcc,y,2))/
    (diff(fAcc,x)**2+diff(fAcc,y)**2)**(3/2)).subs(x,a-h).subs(y,a+h))
)