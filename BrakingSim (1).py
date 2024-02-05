import math
#defining variables
def braking_distance(mass, velocity, road_type, wet_dry, inclination, reaction_time):
#defining constants, Mu values taken from dynamic Mu from slides
    G = 10
    Mu = {
        'asphalt': {'dry': 0.5, 'wet': 0.35},
        #unsure if wet gravel has the same friction as dry gravel, but it only works if I define a value for wet gravel
        'gravel': {'dry': 0.35, 'wet': 0.35},
    }

#assign Mu value to friction
    friction = Mu[road_type][wet_dry]

#modulate it for inclination in rads
    friction *= math.cos(math.radians(inclination))
#formulas with predefined variables, had to ask for help from classmates to derive braking distance
    deceleration = friction * G
    braking_distance = velocity * reaction_time + (velocity**2) / (2 * deceleration)

    return braking_distance
#taking user inputs to assign to variables
mass = float(input("Enter the mass of the car in kg: "))
velocity = float(input("Enter the velocity of the car in m/s: "))
road_type = input("Enter the road type (asphalt/gravel): ")
wet_dry = input("Enter the road condition (wet/dry): ")
inclination = float(input("Enter the inclination of the road in degrees: "))
reaction_time = float(input("Enter the driver's reaction time in seconds: "))

braking_distance = braking_distance(mass, velocity, road_type, wet_dry, inclination, reaction_time)
#print out the result rounding the result to two decimals
print(round(braking_distance, 2))
#additional: code outputs ~20 warnings but works, I'm unsure what most of them are