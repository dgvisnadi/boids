import numpy as np

boids_number = 50
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


def boids_fly_middle(x_coordinate, y_coordinate, velocity_x, velocity_y):
    param = 0.01
    for i in range(boids_number):
        for j in range(boids_number):
            velocity_x[i] = velocity_x[i] + (x_coordinate[j] - x_coordinate[i]) * param / len(x_coordinate)
            velocity_y[i] = velocity_y[i] + (y_coordinate[j] - y_coordinate[i]) * param / len(y_coordinate)
    return velocity_x, velocity_y


def boids_fly_away(x_coordinate, y_coordinate, velocity_x, velocity_y):
    var_multiplier = 2
    var_boundary = 100
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (x_coordinate[i] - x_coordinate[j])
                velocity_y[i] = velocity_y[i] + (y_coordinate[i] - y_coordinate[j])
    return velocity_x, velocity_y

def match_speed(x_coordinate, y_coordinate, velocity_x, velocity_y):
    var_multiplier = 2
    var_boundary = 10000
    param = 0.125
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (velocity_x[j] - velocity_x[i]) * param / len(x_coordinate)
                velocity_y[i] = velocity_y[i] + (velocity_y[j] - velocity_y[i]) * param / len(x_coordinate)
    return velocity_x, velocity_y

def velocity_move(x_coordinate, y_coordinate, velocity_x, velocity_y):
    for i in range(boids_number):
        x_coordinate[i] = x_coordinate[i] + velocity_x[i]
        y_coordinate[i] = y_coordinate[i] + velocity_y[i]
    return x_coordinate, y_coordinate
