from matplotlib import pyplot as plt
from matplotlib import animation
from boids_behavior import *
import random
import seaborn

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

boids_x = [random.uniform(var_x_min, var_x_max) for boid in range(boids_number)]
boids_y = [random.uniform(var_y_min, var_y_max) for boid in range(boids_number)]
boid_x_velocities = [random.uniform(var_velo_x_min, var_velo_x_max) for boid in range(boids_number)]
boid_y_velocities = [random.uniform(var_velo_y_min, var_velo_y_max) for boid in range(boids_number)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

def update_boids(boids):
	boids_x, boids_y, boid_x_velocities, boid_y_velocities = boids
	# Fly towards the middle
	boid_x_velocities, boid_y_velocities = boids_fly_middle(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
	# Fly away from nearby boids
	boid_x_velocities, boid_y_velocities = boids_fly_away(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
	# Try to match speed with nearby boids
	boid_x_velocities, boid_y_velocities = match_speed(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
	# Move according to velocities
	boids_x, boids_y = velocity_move(boids_x, boids_y, boid_x_velocities, boid_y_velocities)


# Prepare Graphic
figure = plt.figure()
figure.suptitle('Boids simulation')

axes = plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter = axes.scatter(boids[0], boids[1])

# Animate and fill graphic
def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))

# Execute boids animation
anim = animation.FuncAnimation(figure, animate,frames=50, interval=50)
# anim.save('animation.gif', writer='imagemagick')

if __name__ == "__main__":
	plt.show()
