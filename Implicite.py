import numpy as np
import matplotlib.pyplot as plt

L=40
v=1
J=50
to=0.01
T=5
N=int(T/to)
h=(2*L)/(J-1)

x = np.linspace(-L,L,J+1)

u=np.zeros(J+1)
for i in range (1,J):
    u[i] = (1/2)+(1/2)*np.tanh((1/(2*np.sqrt(2)))*x[i])

#plt.plot(x, u, 'r', label="u à t=0")
#E = sum(u**2);print(f"E = {E}") # somme des carrés des u[i] à t=0

u_exacte=np.zeros(J+1)
for i in range (1,J):
    u_exacte[i] = (1/2)+(1/2)*np.tanh((1/(2*np.sqrt(2)))*(x[i]+(3/np.sqrt(2))*T))

cst=v*to/h**2
A=np.eye(J-1)
A[0,0]=1+cst
A[J-2,J-2]=1+cst
for i in range(1,J-2):
    A[i,i]=1+2*cst
    A[i-1,i]=-cst
    A[i,i-1]=-cst

up=np.zeros(J+1)
for n in range(1,N):
    secon_terme=u_exacte[1:J]+to*(u_exacte[1:J]*(1-u_exacte[1:J]**2))
    up[1:J]=np.linalg.solve(A,secon_terme)
    u[1:J]=up[1:J]
    
plt.plot(x, up,'b-*', label="schéma")
plt.plot(x, u_exacte, 'r', label="onde prog")
plt.legend( loc = 'upper left')
Ep = sum(up**2);print(f"Ep = {Ep}") # somme des carrés des u[i] à t=tmax

# Erreur :
Erreur = sum(np.abs(up-u_exacte)); print(f"Erreur = {Erreur}")