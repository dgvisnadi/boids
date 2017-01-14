from matplotlib import pyplot as plt
from matplotlib import animation
from boids_code.boids_behavior import *
import seaborn
import yaml

# Variables
config=yaml.load(open("config.yaml"))

boids_number = number
x_min, x_max, y_min, y_max = config['position']
velo_x_min, velo_x_max, velo_y_min, velo_y_max = config['velocity']

boids_x = random_uniform(x_min, x_max, boids_number)
boids_y = random_uniform(y_min, y_max, boids_number)
boid_x_velocities = random_uniform(velo_x_min, velo_x_max, boids_number)
boid_y_velocities = random_uniform(velo_y_min, velo_y_max, boids_number)
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


# Run boids flying behavior
def update_boids(boids):
	boids_x, boids_y, boid_x_velocities, boid_y_velocities = boids
	boid_x_velocities, boid_y_velocities = boids_fly_middle(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
	boid_x_velocities, boid_y_velocities = boids_fly_away(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
	boid_x_velocities, boid_y_velocities = match_speed(boids_x, boids_y, boid_x_velocities, boid_y_velocities)
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
