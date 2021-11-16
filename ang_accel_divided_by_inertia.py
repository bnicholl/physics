#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:12:51 2020

@author: bennicholl
"""
import numpy as np



#Consider the father pushing a playground merry-go-round in Figure 10.38. He exerts
#a force of 250 N at the edge of the 50.0-kg merry-go-round, which has a 1.50-m radius.
#Calculate the angular acceleration produced when no one is on the merry-go-round 

    
force_exerted_by_person = 250 # N

mass_merry_go_round = 50 # kg
radius_merry_go_round = 1.5 # m

inertia =.5 * mass_merry_go_round * radius_merry_go_round ** 2

# the force is radius * force_exerted_by_person * sin, but we dont have sine, so lets assume its 1

net_tourque = force_exerted_by_person * radius_merry_go_round

"""intuition behid this equation: Say net torque, which is radius * F * sin is
1 * 10 * 1 = 20. For simplicity, inerita is 1. Here our angular acceleration is
10 which is directly proportinal to our force. So how big our force is analogous
to how much acceleration we will have on our object. If our radisu is 2, our
angular acceleration doubles!! """
angular_acceleration = net_tourque / inertia


#force_of_moving_merry_go_round = (force_exerted_by_person * radius_merry_go_round) - inertia

#accel = force_of_moving_merry_go_round / mass_merry_go_round








