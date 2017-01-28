from matplotlib import pyplot as plt
from matplotlib import animation
from boids_code.boids import *
import seaborn
import yaml
import os

def make_graph(number, speed, out=False):
    '''Generates an animated plot simulating boids flying.

    Parameters
    ---------
    number: str     - How many boids appear in the animation
    speed: int      - 0 = slow or 1 = fast
    out: str        - Type mp4 or gif to save the animation
    '''


    # Variables
    config=yaml.load(open(os.path.join(os.path.dirname(__file__),'config.yaml')))

    if speed = 0:
        speed = config['velocity']['slow']
    elif speed = 1:
        speed = config['velocity']['fast']

    boids_number = number
    x_min, x_max, y_min, y_max = config['position']
    velo_x_min, velo_x_max, velo_y_min, velo_y_max = speed

    boids_x = random_uniform(x_min, x_max, boids_number)
    boids_y = random_uniform(y_min, y_max, boids_number)
    boid_x_velocities = random_uniform(velo_x_min, velo_x_max, boids_number)
    boid_y_velocities = random_uniform(velo_y_min, velo_y_max, boids_number)
    boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    # Prepare Graphic
    figure = plt.figure()
    figure.suptitle('Flying simulation of boids')
    axes = plt.axes(xlim=(-500,1500), ylim=(-500,1500))
    scatter = axes.scatter(boids[0], boids[1])

    # Animate and fill graphic
    def animate(frame):
       update_boids(boids)
       scatter.set_offsets(list(zip(boids[0],boids[1])))

    # Execute boids animation
    anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

    if out == 'mp4':
        anim.save('boids.mp4')
    if out == 'gif':
        anim.save('boids.gif', writer='imagemagick')
    else:
        plt.show()

    # if __name__ == "__main__":
    #     plt.show()
