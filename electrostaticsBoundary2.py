from sympy.series.series import series
from sympy import *
from matplotlib.pyplot import contour, show
import numpy as np
def coeffList(theta,M):
    a,c = [0 for k in range(M)],round(np.sin(theta)+np.cos(theta),3)
    print("*",c,)
    x = symbols('x')
    f = -log(1-c*x+1/2*x**2)
    f1 = f
    for k in range(M):
        ak = f1.diff(x).doit()
        f1 = ak
        a[k] = round(ak.subs(x,0),3)
    return a
def potent(R,Q,fm,M,x,y):
    e0 = 8.85*10**(-12)
    eps = 10**(-18)
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(x,y)
    s = fm*(R/r)**2*np.sin(2*theta)
    s = s - Q/(4*np.pi*e0)*np.log(
            1-(r/R)*(np.cos(theta)+np.sin(theta))+1/2*(r/R)**2
            )
    a = coeffList(theta,M)
    for m in range(1,M):
        f = (-1)*Q/(4*np.pi*e0)*a[m]*((r/R)**m)
        f = f * (np.cos(m*theta)+np.tan(m*np.pi/(4+eps))*np.sin(m*theta))
        s = s + f
        print("->",m)
    return s
Q = 3.2*10**(-10)
R = 10
n = 20
fm = 0.75
x = np.linspace(0,R,n)
y = np.linspace(0,R,n)
z = [[0 for k in range(n)] for m in range(n)]
for i in range(n):
    for j in range(n):
        print(i,j)
        z[i][j] = potent(R,Q,fm,8,x[i],y[j])
contour(x,y,z,100)
show()