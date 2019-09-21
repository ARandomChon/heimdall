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
EARTH_MASS = 5.792 * 10**24

def Rocket_Equation_Velocity(mass_of_payload, wet_mass, dry_mass, Specific_Impulse):
    mass_of_payload = float(mass_of_payload)
    wet_mass = float(wet_mass)
    dry_mass = float(dry_mass)
    Specific_Impulse = float(Specific_Impulse)


def get_inputs(latitude, longitude):
    print()


def Rocket_Equation_Velocity(mass_of_payload, wet_mass, dry_mass, Specific_Impulse):
    # we calculate the total mass here as we assume that the rocket mass does not include the weight of the payload
    total_mass = wet_mass + mass_of_payload
    # Ve of the RTsiolkovsky rocket equation can be calculated by multiplying
    # the specific impulse times the specific gravity of the earth
    exhaust_velocity = Specific_Impulse*STANDARD_GRAVITY
    # The log of the total wet mass to the dry mass will be calculated thus:
    log_of_wet_to_dry_mass = math.log(total_mass/dry_mass)
    # Thus the equation's delta - v can be calculated by multiplying log and the velocity
    delta_V = exhaust_velocity*log_of_wet_to_dry_mass
    print("The delta-v needed to enter orbit is: ", delta_V, "m/s")
    Energy_needed_for_orbit = (1/2)*total_mass*delta_V*delta_V
    print("The magnitude of energy needed to enter orbit is : ", Energy_needed_for_orbit, "Joules")
    velocity = Specific_Impulse*STANDARD_GRAVITY
    # The log of the total wet mass to the dry mass will be calculated thus:
    log_of_wet_to_dry_mass = math.log(total_mass/dry_mass)
    # Thus the equation's delta - v can be calculated by multiplying log and the velocity
    delta_V = velocity*log_of_wet_to_dry_mass
    return delta_V


def orbitalVelocity(altitude):
    """
    Returns the orbital velocity needed to maintain an orbit
    """
    REarth = CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"]
    g = STANDARD_GRAVITY
    return math.sqrt((g * REarth**2) / (REarth + altitude))

def get_Launch_Coordinates():
    latitude = input("Please enter the latitude of launch location")
    longitude = input("Please enter the longitude of launch location")

# method that takes in velocity and distance or target altitude and spit sout time to establish earth orbit
# redo the main method to handle ona  lop and calll some methods sequentially
# Once we have location of launch, orbital velocity, period, find out how to track location build model
# possible GUI


def Orbital_Period(target_altitude):
    denominator = STANDARD_GRAVITY*(CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"]**2)
    numerator = 4*(CONSTANTS["Universal_Constants"]["PI"]**2)*((CONSTANTS["Earth_Constants"]["EQ_RAD_EARTH"] +
                                                                target_altitude)**3)
    fraction = numerator/denominator
    times = math.sqrt(fraction)
    print("Orbital period of the given body at altitude ", target_altitude, " is :", math.sqrt(fraction), "seconds")
    print("the same time in minutes is : ", times/60)
    print("The same time in hours is   : ", times/(60*60))
    print("The same time in days is    : ", times/(60*60*24))
    return times


def hohmannElliptical(altitudeStart, altitudeEnd):
    """
    Calculate the delta v needed to enter
    elliptical Hohmann transfer orbit
    """
    mu = CONSTANTS["Universal_Constants"]["GRAV_CONST"] * EARTH_MASS
    return math.sqrt(mu/altitudeStart) * (math.sqrt(2*altitudeEnd/(altitudeStart + altitudeEnd)) - 1)


CONSTANTS = {}
#Get Constants
for filename in os.listdir("Constants"):
    if filename.endswith(".json"):
        with open("Constants/" + filename, "r", encoding="utf-8") as fd:
            CONSTANTS[filename.split(".")[0]] = json.load(fd)

