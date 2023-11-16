#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:05:02 2022

@author: carolinephelan

Perceptron Demo
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scstats

points=500
samples=scstats.norm(0,1).rvs([points,2])

x1=samples[:,0]
x2=samples[:,1]
wj=np.zeros([points,2])

adjustment=0.02

comp=x1>x2
y=2*comp.astype(float)-1
x1=x1+y*adjustment
x2=x2-y*adjustment

x=np.zeros([points,2])
x[:,0]=x1
x[:,1]=x2

plt.figure(figsize=(6, 4.5))
ax = plt.axes()
ax.scatter(x1[y==1],x2[y==1],marker='o',c='b')
ax.scatter(x1[y==-1],x2[y==-1],marker='^',c='k')
plt.show()

input('Press Enter')

plt.figure(figsize=(6, 4.5))
ax = plt.axes()
ax.scatter(x1[y==1],x2[y==1],marker='o',c='b')
ax.scatter(x1[y==-1],x2[y==-1],marker='^',c='k')
plt.show()

# initialise w
w=[0.,0.]
A=np.array([2.,-2.])


for i in range(points):
    wj[i,:]=w
    yest=np.sign(np.dot(w,x[i,:]))
    if y[i]==yest:
        plt.scatter(x1[i],x2[i],marker='s',c='g')
        plt.pause(0.001)
    else:
        w=w+y[i]*x[i,:]
        plt.scatter(x1[i],x2[i],marker='s',c='r')
        divisor=np.sqrt(np.dot(w,w))
        ax.plot(w[0]*A/divisor,w[1]*-A/divisor)
        plt.pause(0.01)

    plt.show()
    
plt.figure()
plt.plot(wj[:,0],wj[:,1])
plt.plot(np.array([0.,4.]),np.array([0.,-4.]))
    
B=np.linspace(1,points,num=points)
plt.figure()
plt.plot(B,wj)
    
    


            
    