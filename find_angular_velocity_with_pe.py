#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:38:24 2020

@author: bennicholl
"""
# https://openstax.org/books/university-physics-volume-1/pages/10-5-calculating-moments-of-inertia

from sympy.solvers import solve
from sympy import Symbol


"""this simply shows the integral is equal to how we derive the integral in the below 
find_angular_vel() function """
def brute_force_potential_energy():
    
    cm = 30
    radius_meters = (cm * .01)
    #half_radius_meters = radius_meters / 2
    cosine_of_radians = .86602540378
    
    
    mass = 0.3 # kg
    g = 9.81
    
    
    unit_mass = mass / radius_meters
    
    small_incremental_change = 0.00001
    increasing_radius = 0
    brute_force_pe = 0
    while True:
        increasing_radius += small_incremental_change
        #h = (increasing_radius + (increasing_radius - increasing_radius * cosine_of_radians))
        h = increasing_radius * cosine_of_radians
        pe = (unit_mass * g * h) * small_incremental_change
        """this beow hashtagged pe gives pe at the bottom """
        #pe = (unit_mass * g * increasing_radius) * small_incremental_change
        brute_force_pe += pe
        if increasing_radius >= radius_meters :
            break
        
    print(brute_force_pe)


brute_force_potential_energy()        







# A pendulum in the shape of a rod (Figure 10.30) is released from rest at an angle of  30°.
# It has a length 30 cm and mass 300 g. What is its angular velocity at its lowest point?

def find_angular_vel():
    cm = 30
    radius_meters = (cm * .01)
    """radius_meters / 2 is used for the PE integral, as we can see in the above  brute_force_potential_energy() function"""
    half_radius_meters = radius_meters / 2
    # this is the cosine of a 30 degree angle
    cosine_of_radians = .86602540378
    
    
    mass = 0.3 # kg
    g = 9.81
    """this is what I originally put, and it's wrong, the value under it is correct """
    #h = half_radius_meters + (half_radius_meters - half_radius_meters * cosine_of_radians)
    h = half_radius_meters * cosine_of_radians
    
    potential_energy_at_top = mass * g * h
    print('pe top', potential_energy_at_top)
    potential_energy_at_bottom = mass * g * half_radius_meters
    print('pe bottom', potential_energy_at_bottom)
    print('difference at pe from bottom to top = ', potential_energy_at_top - potential_energy_at_bottom)
    
    ###########################################
    #   we need to find inertia
    
    kg_per_unit_radius = mass / radius_meters
    
    brute_force_inertia_integral = 0
    small_incremental_change = 0.0000001
    increasing_radius = 0
    while True:
        increasing_radius += small_incremental_change
        integral_equation_at_small_inc_change = (increasing_radius ** 2 * kg_per_unit_radius) * small_incremental_change
        brute_force_inertia_integral += integral_equation_at_small_inc_change
        
        if increasing_radius >= radius_meters:
            break
    
    
    # were told w, which is angular velocity == 3.6. Even if we werent told this, since we know all the 
    # other variables in the kinetic energy equation, we could easily solve for w where kinetic energy 
    # equal potential_energy_at_top - potential_energy_at_bottom
    w = 3.6
    #w = 1.65
    kinetic_energy = .5 * brute_force_inertia_integral * w ** 2
    
    print('ke at bottom = ', kinetic_energy)


find_angular_vel()

    
    
    
    

    
    




