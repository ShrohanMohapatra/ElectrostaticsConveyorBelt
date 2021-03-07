from matplotlib.pyplot import contour, show, xlabel, ylabel
import numpy as np
def potent(a,Q,M,x,y):
    e0 = 8.85*10**(-12)
    eps = 10**(-20)
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(x,y)
    s = Q/(4*np.pi*e0)*np.log(2*a**2/((x-a)**2+(y-a)**2))
    s = s - (Q/(8*e0))*(r/a)**2*np.sin(2*theta)
    for m in range(1,M):
        f = (-1)*Q/(4*np.pi*e0)*((r/a)**m)
        f = f * ((1+1j)**m+(1-1j)**m).real/(m*2**m)
        f = f * (np.cos(m*theta)+np.tan(m*np.pi/(4+eps))*np.sin(m*theta))
        s = s + f
        print("->",m,end=" ")
    print()
    return s
Q = -3.2*10**(-10)
a = 10
noOfPoints = 50
noOfContours = 200
maxNoOfTerms = 20
x = np.linspace(-0.01*a,0.99*a,noOfPoints)
y = np.linspace(-0.01*a,0.99*a,noOfPoints)
z = [[0 for k in range(noOfPoints)] for m in range(noOfPoints)]
for i in range(noOfPoints):
    for j in range(noOfPoints):
        print("x = ",x[i],"y = ",y[j])
        z[i][j] = potent(a,Q,maxNoOfTerms,x[i],y[j])
contour(x,y,z,[0.11*k for k in range(noOfContours)],origin="lower")
xlabel('x position (in meters)')
ylabel('y position (in meters)')
show()