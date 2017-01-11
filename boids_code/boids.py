from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Variables
var_range = 50

var_x_min = -450
var_x_max = 50
var_y_min = 300
var_y_max = 600

var_velo_x_min = 0
var_velo_x_max = 10
var_velo_y_min = -20
var_velo_y_max = 20

boids_x = [random.uniform(var_x_min, var_x_max) for x in range(var_range)]
boids_y = [random.uniform(var_y_min, var_y_max) for x in range(var_range)]
boid_x_velocities = [random.uniform(var_velo_x_min, var_velo_x_max) for x in range(var_range)]
boid_y_velocities = [random.uniform(var_velo_y_min, var_velo_y_max) for x in range(var_range)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


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
