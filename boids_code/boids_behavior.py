import numpy as np
import random


# boids_number = 50
# class Boids_fly(object):
#     # def __init__(self, start, end):
#     #     self.start=start
#     #     self.end=end
#     #
#     x_coordinate, y_coordinate, velocity_x, velocity_y = object

def random_uniform(min_values, max_values, boids_number):
    vector = [random.uniform(min_values, max_values) for boid in range(boids_number)]
    return vector

def boids_fly_middle(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    param = 0.01
    for i in range(boids_number):
        for j in range(boids_number):
            velocity_x[i] = velocity_x[i] + (x_coordinate[j] - x_coordinate[i]) * param / len(x_coordinate)
            velocity_y[i] = velocity_y[i] + (y_coordinate[j] - y_coordinate[i]) * param / len(y_coordinate)
    return velocity_x, velocity_y

# Fly away from nearby boids
def boids_fly_away(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    var_multiplier = 2
    var_boundary = 100
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (x_coordinate[i] - x_coordinate[j])
                velocity_y[i] = velocity_y[i] + (y_coordinate[i] - y_coordinate[j])
    return velocity_x, velocity_y

# Try to match speed with nearby boids
def match_speed(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    var_multiplier = 2
    var_boundary = 10000
    param = 0.125
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (velocity_x[j] - velocity_x[i]) * param / len(x_coordinate)
                velocity_y[i] = velocity_y[i] + (velocity_y[j] - velocity_y[i]) * param / len(x_coordinate)
    return velocity_x, velocity_y

# Move according to velocities
def velocity_move(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    for i in range(boids_number):
        x_coordinate[i] = x_coordinate[i] + velocity_x[i]
        y_coordinate[i] = y_coordinate[i] + velocity_y[i]
    return x_coordinate, y_coordinate
