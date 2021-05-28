# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:05:53 2021

@author: annat
"""
import numpy as np 
import matplotlib.pyplot as plt

x = 0.5
a= 1
h = 0.5
t=0 
#numerisch 
arrayx = np.arange(0,7,h)
arrayt = np.arange(0,7,h)

for i in range (arrayx.size):
    arrayx[i]= x 
    x = x - h*x*a
    print(x)
    arrayt[i] = t
    print(t)
    t+= h
    
plt.plot(arrayt, arrayx)
plt.show()
 
#analytisch
x1 = 0.5 
a1 =1 
h1 = 0.002
t1= 0 
arrayt1 = np.arange(0,7,h1)
arrayx1 = np.arange(0,7,h1)
for j in range(arrayx1.size):
    arrayt1[j] = t1
    arrayx1[j] = x1* (pow(np.e, -a*t1))
    t1 += h1
    
plt.plot(arrayt1, arrayx1)
plt.show()

    
    