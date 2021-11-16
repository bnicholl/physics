#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:51:44 2021

@author: bennicholl
"""

from sympy.solvers import solve
from sympy import Symbol
y = Symbol('y')
#solve(y * 5 + 2, y)


def get_x_y_for_quarter_circle():
    
    x_list = []
    y_list = []
    
    radius = 2   
    merry_go_round_radius_x = 2
    merry_go_round_radius_y = [0, 0]
    small_incremental_change = 0.001
    iterations = 0
    
    
    while merry_go_round_radius_x > 0:
        x_list.append(merry_go_round_radius_x)
        y_list.append(merry_go_round_radius_y[1])
        iterations += 1
        
        merry_go_round_radius_x -= small_incremental_change
        try:
            merry_go_round_radius_y = solve( ((merry_go_round_radius_x ** 2 + y ** 2) ** .5) - radius, y )
            #print('c',merry_go_round_radius_x)
            #print('d',merry_go_round_radius_y)
        except:
            #print('a',merry_go_round_radius_x)
            #print('b',merry_go_round_radius_y)
            pass
        
    
    print(merry_go_round_radius_x)
    print(merry_go_round_radius_y)
    
    return x_list, y_list, iterations

x_list, y_list, iterations = get_x_y_for_quarter_circle()
    

def get_inertia_of_solid_circle(merry_go_round_radius_x_li, merry_go_round_radius_y_li, iterations):
    total_inertia_integral = 0
    
    merry_go_round_kg = 500
    radius = 2
    kg_scaled = merry_go_round_kg / radius
    divide_kg_by_previous_iterations = kg_scaled / iterations
    small_incremental_change = 0.001
    
    for x, y in zip(merry_go_round_radius_x_li, merry_go_round_radius_y_li):
        
        if x > y:
            scaler = y/x
            longer_dimension = x
            #shorter_dimension = y
        elif y < x:
            scaler = x/y
            longer_dimension = y
            #shorter_dimension = x
        else:
            # could be either x or y
            longer_dimension = x
            scaler = 1
        
        
        increasing_radius = 0
        while increasing_radius < longer_dimension:
            increasing_radius += small_incremental_change
            longer_dim_inertia = (increasing_radius ** 2 * divide_kg_by_previous_iterations) * small_incremental_change
            shorter_dim_inertia = ((increasing_radius * scaler) ** 2 * divide_kg_by_previous_iterations) * small_incremental_change
            
            inertia = longer_dim_inertia + shorter_dim_inertia
            total_inertia_integral += inertia
    
    print('total inertia of quarter merry go round is: ', total_inertia_integral)
    print("so, total inertia of full merry go round is", total_inertia_integral * 4)
    return total_inertia_integral
    
    
    
    
    
#inert = get_inertia_of_solid_circle(x_list, y_list, iterations)
    





    
    
    
    
    
    
    
    
    