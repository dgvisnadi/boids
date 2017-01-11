from matplotlib import pyplot as plt
from matplotlib import animation
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

def boids_fly_middle(coordinates, velocity):
    param = 0.01
    for iter_i in range(len(coordinates)):
        for iter_j in range(len(coordinates)):
            velocity[iter_i] = velocity[iter_i] + (coordinates[iter_j] - coordinates[iter_j]) \
                                * param / len(coordinates)

def boids_fly_away(boids):
    xs,ys,xvs,yvs=boids
    var_multiplier = 2
    var_boundary = 100
    for boid_i in range(boids_number):
        for boid_j in range(boids_number):
            if (xs[boid_j]-xs[boid_i])**var_multiplier + (ys[boid_j]-ys[boid_i])**var_multiplier < var_boundary:
                xvs[boid_i]=xvs[boid_i]+(xs[boid_i]-xs[boid_j])
                yvs[boid_i]=yvs[boid_i]+(ys[boid_i]-ys[boid_j])

def match_speed(boids):
    xs,ys,xvs,yvs=boids
    var_multiplier = 2
    var_boundary = 10000
    param = 0.125
    for iter_i in range(boids_number):
        for iter_j in range(boids_number):
            if (xs[j]-xs[i])**var_multiplier + (ys[j]-ys[i])**var_multiplier < var_boundary:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*param/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*param/len(xs)

def velocity_move(boids):
    xs,ys,xvs,yvs=boids
    for i in range(boids_number):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]

def update_boids(boids):
    xs,ys,xvs,yvs=boids	
    # Fly towards the middle
    boids_fly_middle(xs, xvs)
    boids_fly_middle(ys, yvs)
    # Fly away from nearby boids
    boids_fly_away(boids)
    # Try to match speed with nearby boids
    match_speed(boids)
    # Move according to velocities
    velocity_move(boids)


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
