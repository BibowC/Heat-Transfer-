# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 06:59:51 2022

@author: Carlos Eduardo Bibow Corrêa
"""
    
import numpy as np
import matplotlib.pyplot as plt

maxIter = 500

xlen = 10
ylen = 10

delta = 1

#contorno
Ttop = 500
Tbot = 800
Tlef = 30
Trig = 30

Tinit = 30

colorint =  50
colormap = plt.cm.jet

#mesh

X, Y = np.meshgrid (np.arange(0, xlen), np.arange(0,ylen))

T = np.empty((xlen, ylen))
T.fill(Tinit)

#contorno

print("espera ai mano pf")

T[(ylen-1):,:] = Ttop
T[:1,:] = Tbot
T[:,(xlen-1):] = Trig
T[:,:1] = Tlef

for iteration in range(0, maxIter):
    for i in range(1, xlen-1, delta):
        for j in range(1, ylen-1, delta):
            T[i,j] = 0.25*(T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
            
print ("blz é isto")

plt.title("Temperatura")
plt.contourf(X, Y, T, colorint, cmap = colormap)
plt.colorbar()
plt.show()