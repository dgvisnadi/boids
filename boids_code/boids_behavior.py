import numpy as np

class Boids_fly(object):
    # def __init__(self, start, end):
    #     self.start=start
    #     self.end=end
    #
    #
    # def geolocate(self, place):
    #     return self.geocoder.geocode(place,
    #             exactly_one=False)[0][1]
    #
    # def location_sequence(self, start,end,steps):
    #     lats = np.linspace(start[0], end[0], steps)
    #     longs = np.linspace(start[1],end[1], steps)
    #     return np.vstack([lats, longs]).transpose()


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
