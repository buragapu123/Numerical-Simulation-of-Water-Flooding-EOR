import numpy as np
import matplotlib.pyplot as plt

n=1000   # number of grids
w=0.001   #  "enter water viscosity"
o=0.00392 # oil viscosity 
ct=0.00000000145 # total compressibility

phi=0.25   # porosity
l=1  # length
del_x=l/n # delta length
A=0.0625 # enter area of reservior 
Q=0.0001378 # enter water flow rate:  75 bbl/day
k=1e-13 # absolute permeability

# left boundary condition

R=(Q*w*del_x)/(A*k) # del p / del x
print(R)

t=1000 # no. of time steps
x=1
y=1
dt=1e-4
r=((k*dt)/((del_x**2)*phi*ct*w))
#r=200
print(r)
z=14000000#float(input("initial pressure = "))
a=np.zeros((n,n))
b=np.zeros((n,n))
c=np.zeros((n,1))
d=np.zeros((n,1))

for i in range(n):
     if i==0:
          a[i,:]= [-r if j==i-1 or j==i+1 else 2+r if j==i else 0 for j in range(n)]
          b[i,:]= [r if j==i-1 or j==i+1 else 2-r if j==i else 0 for j in range(n)]
          d[i,:]=[ z for j in range(1)]
     elif i==n-1:
        a[i,:]= [-r if j==i-1 or j==i+1 else 2+r if j==i else 0 for j in range(n)]
        b[i,:]= [r if j==i-1 or j==i+1 else 2-r if j==i else 0 for j in range(n)]
        d[i,:]=[ z for j in range(1)]
     else:
        a[i,:]= [-r if j==i-1 or j==i+1 else 2+2*r if j==i else 0 for j in range(n)]
        b[i,:]= [r if j==i-1 or j==i+1 else 2-2*r if j==i else 0 for j in range(n)]
        d[i,:]=[ z for j in range(1)]
    
c[0][0]=2*r*R
     
while x<=t: 
     B=np.dot(b,d) 
     G=B+c
     d=np.linalg.solve(a,G)
     if x%200==0:
          plt.plot(np.linspace(0,l,n),d)
     x=x+y
     print(x)
plt.xlabel('Reservior length in meters')
plt.ylabel(" Pressure ")
plt.title("pressure vs length")
plt.show()