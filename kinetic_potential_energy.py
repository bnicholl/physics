#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:12:51 2020

@author: bennicholl
"""
from sympy.solvers import solve
from sympy import Symbol
 

# shows how we can find the distance traveled for a velocity that starts at 5 * t and ends
# when our area of 5 * t = 10
def dist_travelled():
    
    distance_travelled = 0
    
    t = 0.0001
    incremental_small_vallue = 0.0001
    
    
    while True:
        
        velocity_y_val = 20 - (9.81 * t)
        
        multiply_by_x_val = velocity_y_val * incremental_small_vallue
        
        distance_travelled += multiply_by_x_val
        
        if t >= 1.2:
            print('t', t)
            print(distance_travelled)
            break
        
        t += incremental_small_vallue
        
        
        
#dist_travelled()
        
    
    
    


# accel_from_cannon is acceleration of ball after being shot and leaving a cannon
def ke(accel_from_cannon = 20, g = 9.81, mass = 1, check_energy_at_this_meter = 15):
    
    """
    height = 0

    time = 1
    
    # pe = mass * -g * h, if h = sum(accel_from_cannon  - (g * t) * small_incremental_t), the
    # sum over the small_incremental_t part is essiential in creating the AOC, which is what gives us
    # the distance travveled(dist_travelled() func above codes this concept). instead of the equation 
    # i just wrote, we could just use mass * -g * the antiderivative of velocity which is:
    # mass * -g * integral(velocity) = integral(mass * -g * velocity)
    # so the derivative of KE is mass * -g * velocity, then we just integrate mass * -g * velocity
    h = accel_from_cannon  - (g * time)
    pe = mass * -g * h
    
    ke = .5 * mass * (accel_from_cannon  - g * time) ** 2
    # derivative of ke: mass * (accel_from_cannon + -g * time) * -g = 
    # mass * -g * (accel_from_cannon - g * time) or mass * -g * velocity
    # notice the above derivative integrated =  potential energy
    """
    
    t = Symbol('x')
    
    # step 1 use the integral of velocity find out the time it took to travel 15(check_energy_at_this_meter variable) meters
    time_to_go_x_meters = solve((20 * t - 4.905 * t ** 2) - check_energy_at_this_meter )[0]
    
    # step 2 calculate kinetic energy and potential energy using the above time_to_go_x_meters value
    ke = .5 * mass * (accel_from_cannon  - g * time_to_go_x_meters) ** 2
    # below h variable is the integral of velocity, where velocity is: accel_from_cannon - (g * t)
    h = 20 * time_to_go_x_meters - 4.905 * time_to_go_x_meters ** 2
    pe = mass * -g * h
    
    # step 3 calculate how many meters the ball went when the velocity of that ball is at 0, thus
    # signifying our ball is begining to come down!
    time_at_zero_velocity = solve(accel_from_cannon - (g * t))[0]  
    
    # step 4: use the above time_at_zero_velocity var to see how many meters were travelled at the time
    # velocity = 0 by using the integral of velocity beloew
    h_at_zero_velocity = 20 * time_at_zero_velocity - 4.905 * time_at_zero_velocity ** 2
    

    # step 5 use the integral of velocity going down to solve for when the ball is 15(check_energy_at_this_meter) meters away from the ground
    # integral of velocity will be biased by h_at_zero_velocity and check_energy_at_this_meter
    time_ball_x_meters_from_ground = solve((h_at_zero_velocity - 4.905 * t ** 2) - check_energy_at_this_meter)[1]
    
    
    # step 6 calculate kinetic energy and potential energy
    ke_going_down = .5 * mass * (-g * time_ball_x_meters_from_ground) ** 2
    # below h_of_pe_going_down variable is the integral of velocity biased by h_at_zero_velocity, where velocity is: accel_from_cannon - (g * t)
    h_of_pe_going_down = h_at_zero_velocity - (4.905 * time_ball_x_meters_from_ground ** 2)
    pe_going_down = mass * -g * h_of_pe_going_down
    
    
    #print(round(time_at_zero_velocity, 4))
    #print(time_ball_x_meters_from_ground)
    
    print(ke)
    print(pe)
    
    print(ke_going_down)
    print(pe_going_down)
    
    print('this shows energy conserved:',  200 + pe)
    
    
ke()
    


