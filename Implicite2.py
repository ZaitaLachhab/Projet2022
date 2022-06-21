import numpy as np
import matplotlib.pyplot as plt

L=40
v=1
J=50
to=0.01
T=5
N=int(T/to)
h=(2*L)/(J-1)

x = np.linspace(-L,L,J)

u=np.zeros(J)
for i in range (1,J-1):
    if abs(x[i])<=10:
        u[i] = 0.8*np.cos((np.pi*x[i])/20)
    else:
        u[i]=0
u2=u.copy()
#plt.plot(x, u, 'r', label="u à t=0")
#E = sum(u**2);print(f"E = {E}") # somme des carrés des u[i] à t=0

cst=v*to/h**2
A=np.eye(J-2)
A[0,0]=1+cst
A[J-3,J-3]=1+cst
for i in range(1,J-3):
    A[i,i]=1+2*cst
    A[i-1,i]=-cst
    A[i,i-1]=-cst

up=np.zeros(J)
for n in range(1,N):
    secon_terme=u[1:J-1]+to*(u[1:J-1]*(1-u[1:J-1]**2))
    up[1:J-1]=np.linalg.solve(A,secon_terme)
    u[1:J-1]=up[1:J-1]

upp=np.zeros(J)
for n in range(1,N):
    secon_term=u2[1:J-1]+to*(u2[1:J-1]*(1-u2[1:J-1]))
    upp[1:J-1]=np.linalg.solve(A,secon_term)
    u2[1:J-1]=upp[1:J-1]

plt.plot(x, up,'b-*', label="g(u)=u(1-u$^2$)")
plt.plot(x, upp,'r-v', label="g(u)=u(1-u)")
plt.legend( loc = 'upper left')
#Ep = sum(up**2);print(f"Ep = {Ep}") # somme des carrés des u[i] à t=tmax

# Erreur :
#Erreur = sum(np.abs(up-u_exacte)); print(f"Erreur = {Erreur}")