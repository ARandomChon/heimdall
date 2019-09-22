"""
Authors: Sri Kamal Chillarage, kvc9128@rit.edu
         Chris Cheney, cjc1294@rit.edu
         Sean Bergen, sdb2139@rit.edu
         Copyright 2019
orbital-calculations.py
Functions to calculate various numbers
"""
import math
import json
import os

STANDARD_GRAVITY = 9.80665
EARTH_MASS = 5.792 * 10 ** 24


def Rocket_Equation_Velocity(mass_of_payload, wet_mass, dry_mass, Specific_Impulse):
    """
    This is a rudimentary rocket equation calculator that returns the velocity change without accounting for
    gravitational or aerodynamic gravity
    :param mass_of_payload:
    :param wet_mass:
    :param dry_mass:
    :param Specific_Impulse:
    :return: the change in velocity needed
    """
    mass_of_payload = float(mass_of_payload)
    wet_mass = float(wet_mass)
    dry_mass = float(dry_mass)
    Specific_Impulse = float(Specific_Impulse)
    # we calculate the total mass here as we assume that the rocket mass does not include the weight of the payload
    total_mass = wet_mass + mass_of_payload
    # Ve of the RTsiolkovsky rocket equation can be calculated by multiplying
    # the specific impulse times the specific gravity of the earth
    exhaust_velocity = Specific_Impulse * STANDARD_GRAVITY
    # The log of the total wet mass to the dry mass will be calculated thus:
    log_of_wet_to_dry_mass = math.log(total_mass / dry_mass)
    # Thus the equation's delta - v can be calculated by multiplying log and the velocity
    delta_V = exhaust_velocity * log_of_wet_to_dry_mass
    print("The delta-v needed to enter orbit is: ", delta_V, "m/s")
    Energy_needed_for_orbit = (1 / 2) * total_mass * delta_V * delta_V
    print("The magnitude of energy needed to enter orbit is : ", Energy_needed_for_orbit, "Joules")
    velocity = Specific_Impulse * STANDARD_GRAVITY
    # The log of the total wet mass to the dry mass will be calculated thus:
    log_of_wet_to_dry_mass = math.log(total_mass / dry_mass)
    # Thus the equation's delta - v can be calculated by multiplying log and the velocity
    delta_V = velocity * log_of_wet_to_dry_mass
    return delta_V


def orbitalVelocity(altitude):
    """
    Returns the orbital velocity needed to maintain an orbit
    """
    REarth = CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"]
    g = STANDARD_GRAVITY
    return math.sqrt((g * REarth ** 2) / (REarth + altitude))


def Orbital_Period(target_altitude):
    """
    This method calculates the time period of te satellite's orbital path
    In other words it tells you how long the satellite takes to orbit the earth once
    :param target_altitude:
    :return: the time taken in seconds
    """
    denominator = STANDARD_GRAVITY * (CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"] ** 2)
    numerator = 4 * (CONSTANTS["Universal_Constants"]["PI"] ** 2) * ((CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"] +
                                                                      target_altitude) ** 3)
    fraction = numerator / denominator
    times = math.sqrt(fraction)
    print("Orbital period of the given body at altitude ", target_altitude, " is :", math.sqrt(fraction), "seconds")
    print("the same time in minutes is : ", times / 60)
    print("The same time in hours is   : ", times / (60 * 60))
    print("The same time in days is    : ", times / (60 * 60 * 24))
    return times


def hohmannElliptical(altitudeStart, altitudeEnd):
    """
    Calculate the delta v needed to enter
    elliptical Hohmann transfer orbit
    Returns the increase in velocity needed to enter the Hohmann transfer orbit
    """
    mu = CONSTANTS["Universal_Constants"]["GRAV_CONST"] * EARTH_MASS
    return math.sqrt(mu / altitudeStart) * (math.sqrt(2 * altitudeEnd / (altitudeStart + altitudeEnd)) - 1)


def Time_to_higher_orbit():
    """
    This method calculates the time taken by the satellite to move to the higher orbit
    This is currently hardcoded for travel between earth and mars
    :return:
    """
    r1 = CONSTANTS["Universal_Constants"]["ASTRONOMICAL_UNIT"]
    r2 = r1 * 1.524
    numerator = (r1 + r2) ** 3
    denominator = 8 * CONSTANTS["Universal_Constants"]["GRAV_CONST"] * EARTH_MASS
    fraction = numerator/denominator
    Time_Taken = CONSTANTS["Universal_Constants"]["PI"]*math.sqrt(fraction)
    return Time_Taken


def target_angular_velocity():
    """
    This method calculates the target angular velocity needed to reach a given target planet
    :return:
    """
    r1 = CONSTANTS["Universal_Constants"]["ASTRONOMICAL_UNIT"]
    r2 = r1 * 1.524
    w2 = math.sqrt((CONSTANTS["Universal_Constants"]["GRAV_CONST"] * EARTH_MASS)/(r2**3))
    print("The target angular velocity is: ", w2)
    return w2


def angular_alignment():
    """
    This method calculates the angular alignment between earth and mars under ideal hohmann transfer conditions
    This method will return a constant value, but it is useful to use to check if the angular alignment is equivalent
    to the calculated correct value
    :return:
    """
    time = Time_to_higher_orbit()
    angular_velocity = target_angular_velocity()
    alpha = CONSTANTS["Universal_Constants"]["PI"] - angular_velocity*time
    degree_alpha = (alpha*180)/CONSTANTS["Universal_Constants"]["PI"]
    print("The angular alignment between earth and mars is : ", degree_alpha)
    return degree_alpha


CONSTANTS = {}
# Get Constants
for filename in os.listdir("Constants"):
    if filename.endswith(".json"):
        with open("Constants/" + filename, "r", encoding="utf-8") as fd:
            CONSTANTS[filename.split(".")[0]] = json.load(fd)
