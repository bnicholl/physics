#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:59:04 2021

@author: bennicholl
"""
from sklearn.linear_model import Ridge
import numpy as np


#A  +3.0−𝑛𝐶 + 3.0 −nC charge Q is initially at rest a distance of 10 cm (r1))
#from a  +5.0−𝑛𝐶 + 5.0 −nC charge q fixed at the origin.
# Naturally, the Coulomb force accelerates Q away from q, eventually reaching 15 cm

#1. What is the work done by the electric field between  𝑟1 and  𝑟2
#2. How much kinetic energy does Q have at  𝑟2?

 

k = 9.0 * 10 ** 9

#one coulomb is equal to 1,000,000,000 nanocoulombs
q_nanocoulombs = 5
q = q_nanocoulombs / 1000000000

Q_nanocoulombs = 3
Q = Q_nanocoulombs / 1000000000

#r1 = 10
r1 = 0.10

#r2 = 15
r2 = 0.15



original_potential_energy = (k * q * Q) / r1


ke = 0
for i in range(10000000000000000000000000):
    
    potential_energy = (k * q * Q) / r1 ** 2
    
    ke += potential_energy * .00000001
    
    r1 += .00000001
    
    if i % 500000 == 0:
        print(r1)
        print("{:.9f}". format(potential_energy), 'pe joules')
        print("{:.9f}". format(ke), 'ke joules')
    
    if r1 >= r2:
        #print(r1)
        break


print("{:.9f}". format(ke), 'joules')




    
    
    
    






