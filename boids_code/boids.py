from matplotlib import pyplot as plt
from matplotlib import animation
from boids_behavior import Boids_fly
import random

# Variables
boids_number = 50

var_x_min = -450
var_x_max = 50
var_y_min = 300
var_y_max = 600

var_velo_x_min = 0
var_velo_x_max = 10
var_velo_y_min = -20
var_velo_y_max = 20

boids_x = [random.uniform(var_x_min, var_x_max) for x in range(boids_number)]
boids_y = [random.uniform(var_y_min, var_y_max) for x in range(boids_number)]
boid_x_velocities = [random.uniform(var_velo_x_min, var_velo_x_max) for x in range(boids_number)]
boid_y_velocities = [random.uniform(var_velo_y_min, var_velo_y_max) for x in range(boids_number)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

def update_boids(boids):
    boids_x, boids_y, boid_x_velocities, boid_y_velocities = boids
    boids_fly_middle(boids_x, boid_x_velocities) # Fly towards the middle
    boids_fly_middle(boids_y, boid_y_velocities)
    boids_fly_away(boids)     # Fly away from nearby boids
    match_speed(boids) # Try to match speed with nearby boids
    velocity_move(boids) # Move according to velocities


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
	plt.show()
