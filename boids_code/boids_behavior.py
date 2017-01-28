import numpy as np
import random
import yaml
import os

config=yaml.load(open(os.path.join(os.path.dirname(__file__),'config.yaml')))

def random_uniform(min_values, max_values, boids_number):
    """Creating vector of random values"""
    return [random.uniform(min_values, max_values) for boid in range(boids_number)]

def boids_fly_middle(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    """Boids fly towards the middle."""
    param = config['boids_fly_middle'] ['param']
    for i in range(boids_number):
        for j in range(boids_number):
            velocity_x[i] = velocity_x[i] + (x_coordinate[j] - x_coordinate[i]) * param / len(x_coordinate)
            velocity_y[i] = velocity_y[i] + (y_coordinate[j] - y_coordinate[i]) * param / len(y_coordinate)
    return velocity_x, velocity_y


def boids_fly_away(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    """Fly away from nearby boids."""
    var_multiplier = config['boids_fly_away']['var_multiplier']
    var_boundary = config['boids_fly_away']['var_boundary']
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (x_coordinate[i] - x_coordinate[j])
                velocity_y[i] = velocity_y[i] + (y_coordinate[i] - y_coordinate[j])
    return velocity_x, velocity_y


def match_speed(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    """Try to match speed with nearby boids"""
    var_multiplier = config['match_speed']['var_multiplier']
    var_boundary = config['match_speed']['var_boundary']
    param = config['match_speed']['param']
    for i in range(boids_number):
        for j in range(boids_number):
            if (x_coordinate[j] - x_coordinate[i])**var_multiplier + (y_coordinate[j] - y_coordinate[i])**var_multiplier < var_boundary:
                velocity_x[i] = velocity_x[i] + (velocity_x[j] - velocity_x[i]) * param / len(x_coordinate)
                velocity_y[i] = velocity_y[i] + (velocity_y[j] - velocity_y[i]) * param / len(x_coordinate)
    return velocity_x, velocity_y


def velocity_move(x_coordinate, y_coordinate, velocity_x, velocity_y, boids_number):
    """Move according to velocities"""
    for i in range(boids_number):
        x_coordinate[i] = x_coordinate[i] + velocity_x[i]
        y_coordinate[i] = y_coordinate[i] + velocity_y[i]
    return x_coordinate, y_coordinate
