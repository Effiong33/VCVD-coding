import argparse
import math

def braking_distance(mass, velocity, road_type, wet_dry, inclination, reaction_time):
    G = 10
    Mu = {'asphalt': {'dry': 0.5, 'wet': 0.35}, 'gravel': {'dry': 0.35, 'wet': 0.35}}
    friction = Mu[road_type][wet_dry]
    friction *= math.cos(math.radians(inclination))
    deceleration = friction * G
    braking_distance = velocity * reaction_time + (velocity**2) / (2 * deceleration)
    return braking_distance

def main():
    parser = argparse.ArgumentParser(description='Calculate braking distance of a car.')
    parser.add_argument('--mass', type=float, help='Mass of the car in kg')
    parser.add_argument('--velocity', type=float, help='Velocity of the car in m/s')
    parser.add_argument('--road_type', choices=['asphalt', 'gravel'], help='Type of road (asphalt or gravel)')
    parser.add_argument('--wet_dry', choices=['wet', 'dry'], help='Road condition (wet or dry)')
    parser.add_argument('--inclination', type=float, help='Inclination of the road in degrees')
    parser.add_argument('--reaction_time', type=float, help="Driver's reaction time in seconds")

    args = parser.parse_args()

    braking_distance_result = braking_distance(args.mass, args.velocity, args.road_type,
                                               args.wet_dry, args.inclination, args.reaction_time)

    print(round(braking_distance_result, 2))

if _name_ == "_main_":
    main()
