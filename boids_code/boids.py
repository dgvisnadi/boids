from boids_code.boids_behavior import *


# Run boids flying behavior
def update_boids(boids):
	boids_x, boids_y, boid_x_velocities, boid_y_velocities = boids
	boid_x_velocities, boid_y_velocities = boids_fly_middle(boids_x, boids_y, boid_x_velocities, boid_y_velocities, len(boids_x))
	boid_x_velocities, boid_y_velocities = boids_fly_away(boids_x, boids_y, boid_x_velocities, boid_y_velocities, len(boids_x))
	boid_x_velocities, boid_y_velocities = match_speed(boids_x, boids_y, boid_x_velocities, boid_y_velocities, len(boids_x))
	boids_x, boids_y = velocity_move(boids_x, boids_y, boid_x_velocities, boid_y_velocities, len(boids_x))
