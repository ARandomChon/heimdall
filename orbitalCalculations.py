"""
Authors: Sri Kamal Chillarage, kvc9128@rit.edu
         Chris Cheney, cjc1294@rit.edu
         Sean Bergen, sdb2139@rit.edu
         Copyright 2019
orbital-calculations.py
Functions to calculate various numbers
"""
import math

STANDARD_GRAVITY = 9.80665


def get_inputs(latitude, longitude):
    print()


def Rocket_Equation_Velocity(mass_of_payload, wet_mass, dry_mass, Specific_Impulse):
    # we calculate the total mass here as we assume that the rocket mass does not include the weight of the payload
    total_mass = wet_mass + mass_of_payload
    # Ve of the RTsiolkovsky rocket equation can be calculated by multiplying
    # the specific impulse times the specific gravity of the earth
    velocity = Specific_Impulse*STANDARD_GRAVITY
    # The log of the total wet mass to the dry mass will be calculated thus:
    log_of_wet_to_dry_mass = math.log(total_mass/dry_mass)
    # Thus the equation's delta - v can be calculated by multiplying log and the velocity
    delta_V = velocity*log_of_wet_to_dry_mass
    return delta_V



