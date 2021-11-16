#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:22:49 2021

@author: bennicholl
"""
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')


def get_index_of_refraction_for_unknown_medium():
    #Find the index of refraction for medium 2 in Figure 1.13(a), assuming medium 1 is
    #air and given that the incident angle is  30.0° and the angle of refraction is 22.0°
    
    # The law of refraction is stated in equation form as: n1 * sinθ1 = n2 * sinθ2
    # where n1 and n2 are the indices of refraction for media 1 and 2, and  𝜃1 𝜃2 
    # are the angles between the rays and the perpendicular in media 1 and 2
    
    
    n_for_air = 1.000293
     
    sin_for_30_degrees = 0.5
    
    
    law_of_refraction = n_for_air * sin_for_30_degrees# = n_for_unkown_solution * sin_for_22_degrees
    
    sin_for_22_degrees = 0.375
    
    n_for_unkown_solution = solve(law_of_refraction - (sin_for_22_degrees * x)) 
    
    print("index of refraction for medium 2 is: ", n_for_unkown_solution)
    


get_index_of_refraction_for_unknown_medium()





# What is the critical angle for light traveling in a polystyrene (a type of plastic) pipe surrounded 
# by air? The index of refraction for polystyrene is 1.49.

def get_critical_angle():
    
    solve_for_sin = solve(1.000293 - (1.49 * x))
    print('the sin(',solve_for_sin[0],')^-1', '= 42.2 degrees')
    
    # This result means that any ray of light inside the plastic that strikes the surface at an angle
    # greater than  42.2° is totally reflected(total internal reflection.).
    
get_critical_angle()    
    





