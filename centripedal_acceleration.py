#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:55:35 2020

@author: bennicholl
"""

# The magnitude of the angular velocity, denoted by
#ω , is the time rate of change of the angle
#θ as the particle moves in its circular path.


# Angular velocity can also be referred to as the rotation rate in radians per second.
#second. In many situations, we are given the rotation rate in revolutions/s or cycles/s. 
#To find the angular velocity, we must multiply revolutions/s by  2 * pi
#since there are  2 * pi radians in one complete revolution. 
# Since the direction of a positive angle in a circle is counterclockwise, we 
# take counterclockwise rotations as being positive and clockwise rotations as negative.





#A deep-sea fisherman hooks a big fish that swims away from the boat, pulling the fishing line from his fishing reel. The whole system is initially at rest, and the fishing line unwinds from the reel at a radius of 4.50 cm from its axis of rotation. 
#The reel is given an angular acceleration of  110rad/s2 110 rad/s^2 for 2.00 s

#(a) What is the final angular velocity of the reel after 2 s?
#(b) How many revolutions does the reel make?
def fishing_reel():

    final_angular_velocity = 110 * 2
    radans_to_revolutons = 110 / (3.14 * 2)
    total_revolutions = 8.75 * 2 ** 2
    
    #Now the fisherman applies a brake to the spinning reel, achieving an angular acceleration of  −300rad/s2
    #How long does it take the reel to come to a stop?
    
    #solve for 220 + (-300 * t) = 0
    wheel_stopped = 220 / 300
    


#A centrifuge has a radius of 20 cm and accelerates from a maximum rotation rate of 10,000 rpm to rest in 30 seconds under a 
#constant angular acceleration. It is rotating counterclockwise. What is the magnitude of the total acceleration of a point at 
#the tip of the centrifuge at  t = 29.0s?
#What is the direction of the total acceleration vector?

def centrifuge_centripidal_acceleration():
    centrifuge_radius = .2 # meters
    seconds_to_have_zero_vel = 30
    
    rpm = 10000
    rps = rpm / 60
    angular_velocity = rps * (3.14 * 2) # rad / s
    
    angular_acceleration = angular_velocity / seconds_to_have_zero_vel # rad / s/s
    print(angular_acceleration, 'rad / s/s')
    angular_velocity_at_29_seconds = angular_velocity - (angular_acceleration * 29) # rad / s
    print(angular_velocity_at_29_seconds, 'rad / s')
    
    tangential_velocity_at_29_seconds = angular_velocity_at_29_seconds * centrifuge_radius # m/s
    print(tangential_velocity_at_29_seconds, 'm/s')
    tangential_acceleration = angular_acceleration * centrifuge_radius
    print(tangential_acceleration, 'm/s')
    
    centripidal_acceleration = (tangential_velocity_at_29_seconds ** 2) / centrifuge_radius
    print(centripidal_acceleration, 'm/s/s')
    
    # the centripidal_acceleration and the tangential_acceleration are perpindicular, so we can use euclidean 
    # distance to cacluate the total acceleration
    total_acceleration = (centripidal_acceleration ** 2 + tangential_acceleration ** 2) ** .5
    print(total_acceleration, 'm/s/s')