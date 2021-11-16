#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:06:28 2021

@author: bennicholl
"""
from sympy.solvers import solve
from sympy import Symbol
y = Symbol('y')


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

#x_list, y_list, iterations = get_x_y_for_quarter_circle()
"""here x_list is the cordinate of the x direction in some iteration that is <= radius 
and y_list is some cordinate in the y direction in some iteration that is <= radius.
every x_indice[index] + y_indice[index] == radius"""




def get_inerita(x_list, y_list, iterations):
    total_inertia = 0
    
    kg = 500
    radius = 2
    kg_scaled = kg / radius
    kg_scaled_by_iterations = kg_scaled / iterations
    for x,y in zip(x_list, y_list):
        x_inertia = (x ** 2 * kg_scaled_by_iterations) * 0.001
        y_inertia = (y ** 2 * kg_scaled_by_iterations) * 0.001
        
        inertia = x_inertia + y_inertia
        total_inertia += inertia
    
    
    return total_inertia



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        