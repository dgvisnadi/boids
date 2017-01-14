from matplotlib import pyplot as plt
from boids_code.boids import *
import seaborn
import yaml

def make_graph(number, out=False):
    '''
    Generate a plot showing intensity of green pixels between two locations.

    Parameters
    ---------
    start: str
        Start location name, such as London or Paris

    end: str
        End location name, such as Milan or Madrid

    steps: int
        Number of images between start location and end location

    out: str
        Save as, i.e Desktop/graph.png

    Returns
    ---------
    image

    '''


    # Variables
    config=yaml.load(open(os.path.join(os.path.dirname(__file__),'config.yaml'))

    boids_number = number
    x_min, x_max, y_min, y_max = config['position']
    velo_x_min, velo_x_max, velo_y_min, velo_y_max = config['velocity']

    boids_x = random_uniform(x_min, x_max, boids_number)
    boids_y = random_uniform(y_min, y_max, boids_number)
    boid_x_velocities = random_uniform(velo_x_min, velo_x_max, boids_number)
    boid_y_velocities = random_uniform(velo_y_min, velo_y_max, boids_number)
    boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

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
    anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

    if out:
        anim.save('boids.gif', writer='imagemagick')
    else:
        plt.show()

    if __name__ == "__main__":
        plt.show()
