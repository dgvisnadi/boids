from boids_code.boids_behavior import *
from boids_code.boids import *
from nose.tools import assert_equal
from random import randint
import yaml
import os

# Load parameters for testing
position = config['position']
velocity = config['velocity']['slow']
boids_number = randint(1,100)

x_min, x_max, y_min, y_max = position
velo_x_min, velo_x_max, velo_y_min, velo_y_max = velocity
min_values = [x_min, y_min, velo_x_min, velo_y_min]
max_values = [x_max, y_max, velo_x_max, velo_y_max]
x_coordinate = random_uniform(x_min, x_max, boids_number)
y_coordinate = random_uniform(y_min, y_max, boids_number)
velocity_x = random_uniform(velo_x_min, velo_x_max, boids_number)
velocity_y = random_uniform(velo_y_min, velo_y_max, boids_number)

# Testing functions that compare parameters and outcome in functions
def test_yaml_parameter():
    assert(position[0] < position[1] and position[2] < position[3])
    assert(velocity[0] < velocity[1] and velocity[2] < velocity[3])
    assert(int(boids_number))

def test_random_uniform():
    for value in range(len(min_values)):
        test_vector = random_uniform(min_values[value], max_values[value], boids_number)
        assert(min_value <= min(test_vector) and max(test_vector) <= max_values)
        assert_equal(len(test_vector), boids_number)

def test_boids_fly_middle():
    v_x, v_y = boids_fly_middle(x_coordinate, y_coordinate, velocity_x, velocity_y)
    assert_equal(len(v_x), len(v_y))
    assert_equal(len(v_x), len(x_coordinate))
    assert_equal(len(v_x), len(y_coordinate))
    assert_equal(len(v_x), boids_number)

def test_boids_fly_away():
    v_x, v_y = boids_fly_away(x_coordinate, y_coordinate, velocity_x, velocity_y)
    assert_equal(len(v_x), len(v_y))
    assert_equal(len(v_x), len(x_coordinate))
    assert_equal(len(v_x), len(y_coordinate))
    assert_equal(len(v_x), boids_number)

def test_match_speed():
    v_x, v_y = boids_fly_away(x_coordinate, y_coordinate, velocity_x, velocity_y)
    assert_equal(len(v_x), len(v_y))
    assert_equal(len(v_x), len(x_coordinate))
    assert_equal(len(v_x), len(y_coordinate))
    assert_equal(len(v_x), boids_number)

def test_velocity_move():
    v_x, v_y = velocity_move(x_coordinate, y_coordinate, velocity_x, velocity_y)
    assert_equal(len(v_x), len(v_y))
    assert_equal(len(v_x), len(x_coordinate))
    assert_equal(len(v_x), len(y_coordinate))
    assert_equal(len(v_x), boids_number)
