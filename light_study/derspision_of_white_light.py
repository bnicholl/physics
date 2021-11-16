# THE INDEX OF REFRACTION ALSO DEPENDS ON THE WAVELENGTH, AS WELL AS MEDIUM. smaller wavelengths# will increase the index of refraction. This should be obvious. n = c/v. If our photon is bigger,# it will interact with more molecules in the medium, thus slowing it down and making v smaller.# if v is smaller, the index of refraction, n, increasesfrom sympy.solvers import solvefrom sympy import Symbolsin = Symbol('x')# A beam of white light goes from air into crown glass at an incidence angle of  43.2°# What is the angle between the red (660 nm) and violet (410 nm) parts of the refracted light?incidence_angle = 43.2sine_incidence_angle = 0.682# I would think index_of_refraaction_in_air  should change depending on wavelenght, but i wasnt given differenesindex_of_refraaction_in_air = 1.0red_index_of_refraction_in_glass = 1.512violet_index_of_refraction_in_glass = 1.530# index_of_refraaction_in_air  * sine_incidence_angle == red_index_of_refraction_in_glass * some_sin# index_of_refraaction_in_air  * sine_incidence_angle == violet_index_of_refraction_in_glass * some_sin,# so, we need to find the some_sinfind_sin_for_red = solve(sine_incidence_angle * index_of_refraaction_in_air - (red_index_of_refraction_in_glass * sin))print("sin for red photon is: ", find_sin_for_red)print('angle is 26.81')find_sin_for_violet = solve(sine_incidence_angle * index_of_refraaction_in_air - (violet_index_of_refraction_in_glass * sin))print("sin for violet photon is: ", find_sin_for_violet)print('angle is 26.47')