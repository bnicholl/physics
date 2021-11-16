#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:39:40 2021

@author: bennicholl
"""
from math import sin
from math import cos


h = 6.62607004 * 10-34

m = 9.10938356 * 10-31

pi = 3.14

#h = h / (2 * pi)

"""

# the first term and second term make up the kinetic energy


first_term = -h**2 / (2 * m)

# below is second term, which is the 2nd order derivative of the wave function, psi
# for this term we dont know E yet

second_term = sin( ((2*m*E) ** .5 / h) * l ) * -1
# or write 
second_term = sin(-k * x )# where k is the above ((2*m*E) ** .5 / h) * x )
# for the above second term, when x = 0, our value should be 0, and when
# l = the other end of the box, it should also be 0. This means that
# k * x must equal 3.14 radians, because the sin of 3.14 radians = 0!



E = h ** 2 * pi ** 2 / (2 * m * l)
# we now now E


# first term * second_term = E * psi

# notice the second term should equal -psi

"""




# l can be any length and coresponds to the length of the box
l = 40.10
x = 6

# notice the energy of an electron depends on l, the legth of the space. I believe l
# may act as some tyoe of veloicty constant, similiar to g in gravational kinitic energy
E = (h ** 2 * pi ** 2) / (2 * m * l ** 2)
print('notice our wave function is 0 if x = l') 
psi = sin( (2*m*E) ** .5 / h * x) 
print('wave function = ', psi)




#######################
first_term_ke = -h**2 / (2 * m)
second_term_ke = ( (-2*m*E) / h ** 2 ) * psi # second order derivative of wave function
print("notice the original time independant schrodinger equations, where kinetic energy = the total energy times psi")
print(first_term_ke  * second_term_ke)
print(E * psi)


### IMPORTANT. the only descrpency is that the second_term_ke should equal -psi, since it is the
# second order derivative of psi, but it doesnt equal -psi. Maybe this is due to me not normalizing
# the equation yet 





















