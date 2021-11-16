#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:38:24 2020

@author: bennicholl
"""


# Six small washers are spaced 10 cm apart on a rod of negligible mass and 0.5 m in length. 
# The mass of each washer is 20 g. The rod rotates about an axis located at 25 cm, as shown in 
# Figure 10.19. (a) What is the moment of inertia of the system? (b) If the two washers closest
#  to the axis are removed, what is the moment of inertia of the remaining four washers? (c) If
#  the system with six washers rotates at 5 rev/s, what is its rotational kinetic energy?


def inertia():
    grams_of_ball  = 20
    cm_from_radius_to_first_ball = 5
    kg_of_ball = grams_of_ball * .001
    meters_from_radius_to_first_ball = cm_from_radius_to_first_ball * .01
    
    # I = mr2
    moment_of_inertia = 0
    for i in range(3):
        #calculates ball on left
        moment_of_inertia += kg_of_ball * meters_from_radius_to_first_ball ** 2
        #calculates ball on right
        moment_of_inertia += kg_of_ball * meters_from_radius_to_first_ball ** 2
        meters_from_radius_to_first_ball += 10 * .01
    
    print('moment_of_inertia for all six washers is:', moment_of_inertia)    
    
    
    
    revolutions_per_second = 5
    angular_velocity = revolutions_per_second * (3.14 * 2)
    
    meters_from_radius_to_first_ball = cm_from_radius_to_first_ball * .01
    total_kinetic_energy = 0
    # now we calculate totla kinetic energy
    for i in range(3):
        # below equation is the same as total_kinetic_energy equation below, and is technically written correctly
        # .5 * (kg_of_ball * meters_from_radius_to_first_ball ** 2 * angular_velocity ** 2)
        total_kinetic_energy += .5 * (kg_of_ball * (angular_velocity * meters_from_radius_to_first_ball) ** 2)
        total_kinetic_energy += .5 * (kg_of_ball * (angular_velocity * meters_from_radius_to_first_ball) ** 2)
        
        meters_from_radius_to_first_ball += 10 * .01
    
    print('total rotational kinetic_energy is:', total_kinetic_energy, 'joules')
    
    
#A typical small rescue helicopter has four blades: Each is 4.00 m long and has a mass of 50.0 kg. 
# The blades can be approximated as thin rods that rotate about one end of an axis perpendicular to
# their length. The helicopter has a total loaded mass of 1000 kg. (a) Calculate the rotational kinetic
# energy in the blades when they rotate at 300 rpm. (b) Calculate the translational kinetic energy
# of the helicopter when it flies at 20.0 m/s, and compare it with the rotational energy in the blades.
def helicopter():
    number_of_blades = 4
    length_of_blade = 4 # meters
    mass_of_blade = 50 # kg
    rpm = 300
    
    rps = rpm / 60
    
    angular_velocity = rps * (3.14 * 2)
    print(angular_velocity)
    # notice how this inertia equation takes into account the length of the blade, as opposed to
    # multiplying angular velocity by length of blade in below kinetic energy equation
    inertia = (mass_of_blade * length_of_blade ** 2) / 3
    print(inertia)
    rotational_kinetic_energy = (.5 * inertia * (angular_velocity) ** 2) * number_of_blades
    
    print('rotational kinetic energy',rotational_kinetic_energy)
    
    velocity_of_helicopter_moving = 20 # m/s
    mass_of_helicopter = 1000 # kg
    translational_kinetic_energy = .5 * (mass_of_helicopter * velocity_of_helicopter_moving ** 2)
    print('translational_kinetic_energy', translational_kinetic_energy)
    
    ratio_of_translational_kinetic_energy_to_rotational_kinetic_energy = translational_kinetic_energy / rotational_kinetic_energy
    
    print('ratio_of_translational_kinetic_energy_to_rotational_kinetic_energy', ratio_of_translational_kinetic_energy_to_rotational_kinetic_energy)
    
    
    


    
def brute_force_inertia():  


    """ below code finds moment of inertia for a rod with acis at the end """   
    merry_go_round_kg = 500 # kg
    merry_go_round_radius = 2 # meters
    
    # inertia equation = r ** 2 * m
    # inertia_integral_for one_dimensions = sum(sum(some small radius constant) ** 2 * (weight in kg * sum(some small weight percentage constage))) * (some small radius constant)
    # where, 
    # some some small radius constant sums to 1 and,
    # weight in kg * some small weight percentage constage sums to 500
    # some small radius constant would = some small weight percentage constage only if merry_go_round_radius = 1,
    # if merry_go_round_radius != 1, the equation =
    # sum(sum(some small radius constant) ** 2 * ((merry_go_round_kg / merry_go_round_radius) * some small weight percentage constage)) * (some small radius constant)
    # where 
    # some small radius constant would = some small weight percentage constage
    brute_forced_integral = 0
    
    count_to_merry_go_round_radius = 0
    small_incremental_change = 0.00001
    
    
    # we need to do this because at 1, all of our kg will be accounted for, for example, if our small_incremental_change is .1
    # and our radius is 2, 
    # .1 * 500 = 50, 50 * 10 = 500, as we can see all of our kilograms are accounted for a radius == 1, but our radius is 2,
    # so we need to divide merry_go_round_kg / merry_go_round_radius to remedy this
    kg_per_unit_radius = merry_go_round_kg / merry_go_round_radius
    while True:
        count_to_merry_go_round_radius += small_incremental_change
        brute_forced_integral += (count_to_merry_go_round_radius ** 2 * kg_per_unit_radius) * small_incremental_change
        if count_to_merry_go_round_radius >= merry_go_round_radius:
            break
    print(brute_forced_integral)
    
    
    """now we figure out what moment of inertia would be if merry_go_round_kg stays the same,
    merry_go_round_radius stays the same and intead of a bar, we have a circle """
    
    
def merry_go_round_problem():
    
    child_weight = 25 # kg
    child_radius = 1
    merry_go_round_kg = 500 # kg
    merry_go_round_radius = 2
    child_inertia = child_radius ** 2 * child_weight
    
    ### brute force the integral for the area of a circle
    count_to_merry_go_round_radius = 0
    small_incremental_change = 0.00001
    brute_forced_area_integral = 0
    two_pi = 3.14 * 2
    
    while True:
        count_to_merry_go_round_radius += small_incremental_change
        brute_forced_area_integral += count_to_merry_go_round_radius * two_pi * small_incremental_change
        if count_to_merry_go_round_radius >= merry_go_round_radius:
            break
    print(brute_forced_area_integral)
    # this is the actual integral function
    area_integral = 3.14 * merry_go_round_radius ** 2
    print(area_integral)
    
    
    
    ### brute foprce integral for the inertia of the merry go round and child
    brute_forced_integral = 0
    count_to_merry_go_round_radius = 0
    small_incremental_change = 0.000001    
    kg_per_unit_radius = merry_go_round_kg / area_integral
    
    while True:
        count_to_merry_go_round_radius += small_incremental_change
        #circumference_area = count_to_merry_go_round_radius * 3.14 * 2
        #brute_forced_integral += (count_to_merry_go_round_radius ** 2 * kg_per_unit_radius) * (2 * 3.14 * count_to_merry_go_round_radius)  * small_incremental_change
        brute_forced_integral += count_to_merry_go_round_radius ** 2 * (2 * 3.14 * count_to_merry_go_round_radius)  * kg_per_unit_radius * small_incremental_change
        if count_to_merry_go_round_radius >= merry_go_round_radius:
            break
    print(brute_forced_integral)
    print(brute_forced_integral + child_inertia)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    




