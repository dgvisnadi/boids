import numpy as np

# class Boids_fly(object):
    # def __init__(self, start, end):
    #     self.start=start
    #     self.end=end
    #
    #
    # def geolocate(self, place):
    #     return self.geocoder.geocode(place,
    #             exactly_one=False)[0][1]
    #
    # def location_sequence(self, start,end,steps):
    #     lats = np.linspace(start[0], end[0], steps)
    #     longs = np.linspace(start[1],end[1], steps)
    #     return np.vstack([lats, longs]).transpose()


def boids_fly_middle(coordinates, velocity):
    param = 0.01
    for i in range(50):
        for j in range(50):
            velocity[i]=velocity[i]+(coordinates[j]-coordinates[i])*0.01/len(coordinates)
    return velocity


def boids_fly_away(xs,ys,velocity):
    var_multiplier = 2
    var_boundary = 100
    boids_number = 50
    for boid_i in range(boids_number):
        for boid_j in range(boids_number):
            if (xs[boid_j]-xs[boid_i])**var_multiplier + (ys[boid_j]-ys[boid_i])**var_multiplier < var_boundary:
                velocity[boid_i]=velocity[boid_i]+(xs[boid_i]-xs[boid_j])
    return velocity

def match_speed(xs,ys,velocity):
    boids_number = 50
    var_multiplier = 2
    var_boundary = 10000
    param = 0.125
    for i in range(boids_number):
        for j in range(boids_number):
            if (xs[j]-xs[i])**var_multiplier + (ys[j]-ys[i])**var_multiplier < var_boundary:
                velocity[i]=velocity[i]+(velocity[j]-velocity[i])*param/len(xs)
    return velocity

def velocity_move(coordinates,velocity):
    boids_number = 50
    for i in range(boids_number):
        coordinates[i]=coordinates[i]+velocity[i]
    return coordinates
